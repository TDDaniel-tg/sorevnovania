function updateTimer() {
    const deadline = new Date('2025-05-01T00:00:00');
    const now = new Date();
    const diff = deadline - now;

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    document.querySelector('.timer-container').innerHTML = `
        <div class="timer-segment">
            <div class="timer-value">${String(days).padStart(2, '0')}</div>
            <div class="timer-label">дней</div>
        </div>
        <div class="timer-segment">
            <div class="timer-value">${String(hours).padStart(2, '0')}</div>
            <div class="timer-label">часов</div>
        </div>
        <div class="timer-segment">
            <div class="timer-value">${String(minutes).padStart(2, '0')}</div>
            <div class="timer-label">минут</div>
        </div>
        <div class="timer-segment">
            <div class="timer-value">${String(seconds).padStart(2, '0')}</div>
            <div class="timer-label">секунд</div>
        </div>
    `;
}

setInterval(updateTimer, 1000);
updateTimer();