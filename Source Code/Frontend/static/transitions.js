function pageTransition() {
    var tl = gsap.timeline();
    
    tl.to('.page-transition', {
        duration: 0.5,
        scaleY: 1,
        transformOrigin: 'bottom',
        ease: 'power4.inOut'
    });

    tl.to('.page-transition', {
        duration: 0.5,
        scaleY: 0,
        transformOrigin: 'top',
        ease: 'power4.inOut',
        delay: 0.2
    });
}

function contentAnimation() {
    var tl = gsap.timeline();
    
    tl.from('.container', {
        duration: 0.5,
        translateY: 50,
        opacity: 0,
        delay: 0.5
    });
}

function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

function initializeBarba() {
    barba.init({
        transitions: [{
            name: 'opacity-transition',
            leave(data) {
                return gsap.to(data.current.container, {
                    opacity: 0,
                    duration: 0.5
                });
            },
            enter(data) {
                return gsap.from(data.next.container, {
                    opacity: 0,
                    duration: 0.5
                });
            }
        }],
        views: [{
            namespace: 'page',
            beforeEnter(data) {
                updateActiveNavLink();
            }
        }]
    });
}

// Initialize Barba after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeBarba();
    updateActiveNavLink();
});

// Prevent form submissions from triggering transitions
document.addEventListener('submit', function(e) {
    e.preventDefault();
});

// Handle navigation errors
barba.hooks.after(() => {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});