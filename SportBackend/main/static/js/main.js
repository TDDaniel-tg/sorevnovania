// Добавляем активный класс для текущего пункта меню
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Burger menu toggle
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('header nav');

    burger.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
});