function next() {
    const target = document.querySelector('.landing');
    target.style.setProperty('--bg', 'none');
    target.style.display = 'none';
    
}

document.getElementById('next').addEventListener('click', next);
