// Hides the landing page and saves the user's action
function next() {
    const target = document.querySelector('.landing');
    target.style.setProperty('--bg', 'none');
    target.style.display = 'none';

    // Remember that the user clicked "Next"
    sessionStorage.setItem('visited', 'true');
}

// Checks when the specific div becomes visible and removes extra margin
function checkVisibility() {
    const headingElement = document.getElementById('myUniqueDiv'); // Replace with your unique ID

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove the 'mt-5' class when the specific div is visible
                headingElement.classList.remove('mt-5');
            }
        });
    }, { threshold: 0.5 }); // Trigger when 10% of the element is visible

    observer.observe(headingElement);
}

// Handle the "Next" button click
document.getElementById('next').addEventListener('click', () => {
    next();
    checkVisibility();
});

// Check if the user has visited before when the page loads
window.onload = function () {
    // Scroll to the top of the page
    window.scrollTo(0, 0);

    if (sessionStorage.getItem('visited') === 'true') {
        // Redirect to the home page (or reset the landing page)
        window.location.href = '#';
    }
};



function register() {
  const registerShow = document.getElementById('sign-up');
 const registerBtn = document.getElementById('register');
  registerShow.style.display = 'block';
  registerBtn.style.display = 'none';
}

document.getElementById('register').addEventListener(click, register);