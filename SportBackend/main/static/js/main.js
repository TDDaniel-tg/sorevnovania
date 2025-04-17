// Добавляем активный класс для текущего пункта меню
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('header nav');
    const body = document.body;
    const dropdowns = document.querySelectorAll('.dropdown');
    
    // Добавляем активный класс для текущего пункта меню
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Burger menu functionality
    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        nav.classList.toggle('active');
        body.classList.toggle('menu-open');
    });

    // Handle dropdowns
    dropdowns.forEach(dropdown => {
        const dropdownTrigger = dropdown.querySelector('.dropdown-trigger');
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        
        dropdownTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            // Закрываем все другие дропдауны
            dropdowns.forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('active');
                    otherDropdown.querySelector('.dropdown-menu').classList.remove('show');
                }
            });
            
            // Переключаем текущий дропдаун
            dropdown.classList.toggle('active');
            dropdownMenu.classList.toggle('show');
        });

        // Предотвращаем закрытие при клике на само меню
        dropdownMenu.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // Обработка клика по пунктам меню
        dropdownMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', (e) => {
                e.stopPropagation();
                // Закрываем меню только после перехода по ссылке
                setTimeout(() => {
                    burger.classList.remove('active');
                    nav.classList.remove('active');
                    body.classList.remove('menu-open');
                    dropdowns.forEach(d => {
                        d.classList.remove('active');
                        d.querySelector('.dropdown-menu').classList.remove('show');
                    });
                }, 100);
            });
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!nav.contains(e.target) && !burger.contains(e.target)) {
            burger.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
                dropdown.querySelector('.dropdown-menu').classList.remove('show');
            });
        }
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            burger.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
                dropdown.querySelector('.dropdown-menu').classList.remove('show');
            });
        }
    });
});