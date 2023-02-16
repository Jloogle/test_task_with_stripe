# Тестовое задание 

# Реализация покупки товара с помощью Stripe
Страница с товаром и кнопкой 'Buy' которая реализована как API и после её нажатия JS получает ответ от API и перенаправляет на страницу оплаты с помощью скрипта

## Стек технологий

При разработке использован следующий стек технологий:

* Python 3.10
* Django 4.1.7
* Django Rest Framework
* Sripe
* PostgreSQL
* Docker
* nginx
* Yandex.Cloud

# Порядок запуска
##На локальном компьютере:
Клонируйте репозиторий и перейдите каталок с файлом docker-compose.yaml:
```
git clone git@github.com:Jloogle/test_task_with_stripe.git
```
Создайте и активируйте виртуальное окружение, обновите pip и установите зависимости:
```
python3 -m venv venv
. venv/bin/activate
cd task_with_stripe
python3 -m pip install --upgrade pip
python3 -r requirements.txt
```
Создайте файл .env внутри папки infra:   
Внесите туда переменные окружения:   
```
SECRET_KEY
DB_ENGINE=django.db.backends.postgresql
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
```
Перейдите в папку infra
Запустите сборку контейнера с проектом командой:
```
docker-compose up -d --build
```
Соберите статические файлы (статику):
```
docker-compose exec backend python manage.py collectstatic --no-input
```
Примените миграции:
```
docker-compose exec backend python manage.py makemigrations
```
```
docker-compose exec backend python manage.py migrate --noinput
```
Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
