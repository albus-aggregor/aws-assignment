FROM python:3.9.24-slim

WORKDIR /app

COPY devops /app/
COPY requirements.txt /app/

SHELL ["/bin/bash", "-c"]

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000