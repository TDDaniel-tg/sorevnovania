document.addEventListener('DOMContentLoaded', function() {
    // Установите дату окончания регистрации (25 апреля 2025)
    const endDate = new Date('2025-04-25T23:59:59').getTime();

    function updateTimer() {
        const now = new Date().getTime();
        const distance = endDate - now;

        // Расчет времени
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Обновление значений на странице
        document.querySelector('.timer-value:nth-child(1)').textContent = days.toString().padStart(2, '0');
        document.querySelector('.timer-value:nth-child(2)').textContent = hours.toString().padStart(2, '0');
        document.querySelector('.timer-value:nth-child(3)').textContent = minutes.toString().padStart(2, '0');
        document.querySelector('.timer-value:nth-child(4)').textContent = seconds.toString().padStart(2, '0');

        // Если время истекло
        if (distance < 0) {
            clearInterval(timerInterval);
            document.querySelector('.timer-circle').innerHTML = "Регистрация закрыта";
        }
    }

    // Обновление таймера каждую секунду
    const timerInterval = setInterval(updateTimer, 1000);
    updateTimer(); // Первоначальное обновление
}); 