FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY project/ ./project

RUN mkdir -p /app/instance

RUN python3 project/create_db.py

CMD ["gunicorn", "-b", "0.0.0.0:8000", "project.app:app"]

EXPOSE 8000

