function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('تم استلام رسالتك. شكرا لتواصلك!');
});
