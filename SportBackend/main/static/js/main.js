// Добавляем активный класс для текущего пункта меню
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Burger menu functionality
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('header nav');
    const body = document.body;
    const dropdowns = document.querySelectorAll('.dropdown');

    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        nav.classList.toggle('active');
        body.classList.toggle('menu-open');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!nav.contains(e.target) && !burger.contains(e.target) && nav.classList.contains('active')) {
            burger.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
        }
    });

    // Handle dropdowns in mobile menu
    dropdowns.forEach(dropdown => {
        const dropdownTrigger = dropdown.querySelector('p');
        const dropdownLinks = dropdown.querySelectorAll('.dropdown-menu a');
        
        dropdownTrigger.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                e.stopPropagation();
                dropdown.classList.toggle('active');
            }
        });

        // Предотвращаем закрытие меню при клике на пункты выпадающего списка
        dropdownLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });
    });

    // Close menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            burger.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
        });
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            burger.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
            dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
        }
    });
});