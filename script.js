function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('تم استلام رسالتك. شكرا لتواصلك!');
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

const toTopBtn = document.getElementById('to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        toTopBtn.style.display = 'block';
    } else {
        toTopBtn.style.display = 'none';
    }
});
