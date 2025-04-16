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

    // Handle dropdowns
    dropdowns.forEach(dropdown => {
        const dropdownTrigger = dropdown.querySelector('.dropdown-trigger');
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        
        dropdownTrigger.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent navigation
            dropdown.classList.toggle('active');
            
            // Close other dropdowns
            dropdowns.forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('active');
                }
            });
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.dropdown')) {
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
            });
        }
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