document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registrationForm');
    
    if (registrationForm) {
        registrationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Собираем данные формы
            const formData = new FormData(registrationForm);
            const data = Object.fromEntries(formData.entries());
            
            try {
                // Здесь можно добавить отправку данных на сервер
                // Например:
                // const response = await fetch('/api/register', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/json',
                //     },
                //     body: JSON.stringify(data)
                // });
                
                // Временное решение - просто показываем сообщение об успехе
                alert('Регистрация успешно завершена! Мы свяжемся с вами в ближайшее время.');
                registrationForm.reset();
                
            } catch (error) {
                console.error('Ошибка при отправке формы:', error);
                alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте позже.');
            }
        });
    }
});