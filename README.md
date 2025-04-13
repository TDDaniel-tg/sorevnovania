# Спортивный сайт

## Требования к системе
- Python 3.8 или выше
- pip (менеджер пакетов Python)
- Git

## Установка и настройка

1. Клонирование репозитория
```bash
git clone <url-репозитория>
cd sport
```

2. Создание виртуального окружения
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate
```

3. Установка зависимостей
```bash
pip install -r requirements.txt
```

4. Настройка базы данных
```bash
python manage.py migrate
```

5. Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```

6. Запуск сервера разработки
```bash
python manage.py runserver
```

## Структура проекта
- `SportBackend/` - основная директория проекта
  - `main/` - главное приложение
  - `participants/` - приложение для работы с участниками
  - `media/` - директория для медиафайлов
  - `settings.py` - настройки проекта
  - `urls.py` - основные URL-маршруты

## Основные зависимости
- Django 5.0.2 - веб-фреймворк
- Django REST Framework - для создания API
- django-cors-headers - для настройки CORS
- Pillow - для работы с изображениями
- python-dotenv - для работы с переменными окружения
- django-filter - для фильтрации данных
- djangorestframework-simplejwt - для JWT аутентификации
- psycopg2-binary - для работы с PostgreSQL
- gunicorn - WSGI-сервер для production
- whitenoise - для раздачи статических файлов

## Разработка
1. Создание миграций
```bash
python manage.py makemigrations
```

2. Применение миграций
```bash
python manage.py migrate
```

3. Сбор статических файлов
```bash
python manage.py collectstatic
```

## Деплой
1. Настройка переменных окружения
```bash
# Создайте файл .env в корневой директории
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
```

2. Запуск production-сервера
```bash
gunicorn SportBackend.wsgi:application
```

## Техническая поддержка
При возникновении проблем:
1. Проверьте логи в `debug.log`
2. Убедитесь, что все зависимости установлены
3. Проверьте настройки в `settings.py`
4. Обратитесь к администратору системы

## Лицензия
MIT License

## Описание
Веб-приложение для управления спортивными мероприятиями и тренировками. Проект состоит из бэкенд-части, разработанной на Python.

## Технологии
- Python
- Backend Framework (уточнить)
- База данных (уточнить)

## Разработка
Для начала работы над проектом:
1. Создайте новую ветку для ваших изменений
2. Внесите необходимые изменения
3. Создайте pull request

## Контакты
[Указать контактную информацию] 