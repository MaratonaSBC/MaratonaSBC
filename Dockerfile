FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]

