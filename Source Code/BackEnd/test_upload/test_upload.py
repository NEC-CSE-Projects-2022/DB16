import requests

def test_upload():
    url = 'http://localhost:5000/upload'
    with open('test.pdf', 'rb') as f:
        files = {'pdf': f}
        response = requests.post(url, files=files)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

if __name__ == '__main__':
    test_upload()