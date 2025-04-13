document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registrationForm');
    
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Получение данных формы
            const formData = {
                name: document.querySelector('input[name="name"]').value,
                phone_number: document.querySelector('input[name="phone_number"]').value,
                city: document.querySelector('input[name="city"]').value,
                weight_category: parseInt(document.querySelector('input[name="weight_category"]').value),
                age: parseInt(document.querySelector('input[name="age"]').value),
                discipline: document.querySelector('input[name="discipline"]').value
            };
            
            // Здесь можно добавить валидацию данных
            if (!validateForm(formData)) {
                return;
            }
            
            // Отправка данных на сервер
            fetch('/participants/api/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showMessage(data.message, 'success');
                    registrationForm.reset();
                    setTimeout(() => {
                        window.location.href = '/participants/';
                    }, 2000);
                } else {
                    showMessage(data.message || 'Произошла ошибка при регистрации', 'error');
                }
            })
            .catch(error => {
                showMessage('Произошла ошибка при отправке данных', 'error');
                console.error('Error:', error);
            });
        });
    }
    
    // Функция валидации формы
    function validateForm(data) {
        if (!data.name || data.name.trim() === '') {
            showMessage('Пожалуйста, введите ФИО', 'error');
            return false;
        }
        
        if (!data.phone_number || !isValidPhone(data.phone_number)) {
            showMessage('Пожалуйста, введите корректный номер телефона в формате +996XXXXXXXXX или +996 XXXXXXXX', 'error');
            return false;
        }
        
        if (!data.city || data.city.trim() === '') {
            showMessage('Пожалуйста, введите город', 'error');
            return false;
        }
        
        if (!data.weight_category || data.weight_category < 30 || data.weight_category > 150) {
            showMessage('Пожалуйста, введите корректную весовую категорию (30-150 кг)', 'error');
            return false;
        }
        
        if (!data.age || data.age < 6 || data.age > 100) {
            showMessage('Пожалуйста, введите корректный возраст (6-100 лет)', 'error');
            return false;
        }
        
        if (!data.discipline || data.discipline.trim() === '') {
            showMessage('Пожалуйста, введите дисциплину', 'error');
            return false;
        }
        
        return true;
    }
    
    // Вспомогательные функции
    function isValidPhone(phone) {
        const re = /^\+996\s*[0-9]{9}$/;
        return re.test(phone);
    }
    
    function showMessage(message, type) {
        const messageDiv = document.getElementById('message');
        if (messageDiv) {
            messageDiv.textContent = message;
            messageDiv.style.color = type === 'success' ? 'green' : 'red';
        } else {
            const newMessageDiv = document.createElement('div');
            newMessageDiv.id = 'message';
            newMessageDiv.className = `message ${type}`;
            newMessageDiv.textContent = message;
            newMessageDiv.style.color = type === 'success' ? 'green' : 'red';
            
            const form = document.querySelector('.form-container');
            form.parentNode.insertBefore(newMessageDiv, form.nextSibling);
            
            setTimeout(() => {
                newMessageDiv.remove();
            }, 5000);
        }
    }
}); 