  document.addEventListener('DOMContentLoaded', () => {
    const phoneInput = document.querySelector('input[name="number"]');
    
    phoneInput.addEventListener('focus', () => {
      if (phoneInput.value === '') {
        phoneInput.value = '+996';
        phoneInput.style.color = 'black';
      }
    });

    phoneInput.addEventListener('input', () => {
      if (!phoneInput.value.startsWith('+996')) {
        phoneInput.value = '+996';
      }
    });

    phoneInput.addEventListener('blur', () => {
      if (phoneInput.value === '+996') {
        phoneInput.value = '';
        phoneInput.placeholder = 'Введите номер';
        phoneInput.style.color = 'black';
      }
    });
  });