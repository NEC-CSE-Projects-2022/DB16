from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch
from flask_cors import CORS
import logging
import fitz
import io
import os
import traceback

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize model
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# Store PDF content
pdf_content = ""

# Navigation Routes
@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/trybot')
def trybot():
    return render_template('home.html', active_page='trybot')

@app.route('/about')
def about():
    return render_template('About.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('Projects.html', active_page='projects')

@app.route('/contact')
def contact():
    return render_template('Contact.html', active_page='contact')

# API Routes
@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_content
    try:
        logger.debug("Upload request received")
        
        if 'pdf' not in request.files:
            logger.error("No PDF file in request")
            return jsonify({'error': 'No PDF file uploaded'}), 400
        
        file = request.files['pdf']
        if file.filename == '':
            logger.error("No filename")
            return jsonify({'error': 'No file selected'}), 400

        # Read and process PDF content
        try:
            pdf_bytes = file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            extracted_text = ""
            for page in pdf_document:
                extracted_text += page.get_text()
            pdf_document.close()
            
            # Store the extracted text
            pdf_content = extracted_text
            
            logger.debug(f"Successfully processed PDF, content length: {len(pdf_content)}")
            return jsonify({
                'message': 'File uploaded successfully'
            })
            
        except Exception as pdf_error:
            logger.error(f"PDF processing error: {traceback.format_exc()}")
            return jsonify({'error': 'Invalid PDF file or processing error'}), 400

    except Exception as e:
        logger.error(f"Upload error: {traceback.format_exc()}")
        return jsonify({'error': 'Server error processing upload'}), 500

@app.route('/ask', methods=['POST'])
def ask():
    global pdf_content
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Question is required'}), 400
            
        if not pdf_content:
            return jsonify({'error': 'Please upload a PDF first'}), 400

        question = data['question']
        
        # Limit context size and ensure it's string
        context = str(pdf_content[:4000])
        prompt = f"Question: {question}\nContext: {context}\nAnswer:"
        
        try:
            response = qa_pipeline(prompt, max_length=100, num_return_sequences=1)
            answer = response[0]['generated_text']
            
            return jsonify({
                'question': question,
                'answer': answer
            })
        except Exception as model_error:
            logger.error(f"Model error: {traceback.format_exc()}")
            return jsonify({'error': 'Error generating answer'}), 500

    except Exception as e:
        logger.error(f"Ask error: {traceback.format_exc()}")
        return jsonify({'error': 'Server error processing question'}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logger.error(f"Startup error: {traceback.format_exc()}")
