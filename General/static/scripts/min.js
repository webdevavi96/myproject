// Hides the landing page and saves the user's action
function next() {
    const target = document.querySelector('.landing');
    target.style.setProperty('--bg', 'none');
    target.style.display = 'none';

    // Remember that the user clicked "Next"
    sessionStorage.setItem('visited', 'true');
}

// Checks when the <h1> element becomes visible and removes extra margin
function checkVisibility() {
    const headingElement = document.querySelector('h1.mt-5');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove the 'mt-5' class when <h1> is visible
                headingElement.classList.remove('mt-5');
            }
        });
    }, { threshold: 0.1 }); // Trigger when 10% of the element is visible

    observer.observe(headingElement);
}

// Handle the "Next" button click
document.getElementById('next').addEventListener('click', () => {
    next();
    checkVisibility();
});

// Check if the user has visited before when the page loads
window.onload = function () {
    if (sessionStorage.getItem('visited') === 'true') {
        // Redirect to the home page (or reset the landing page)
        window.location.href = '/General/templates/index.html';
    }
};
