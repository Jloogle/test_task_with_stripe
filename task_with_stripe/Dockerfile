FROM python:3.10.5-slim

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "task_with_stripe.wsgi:application", "--bind", "0:8000"]