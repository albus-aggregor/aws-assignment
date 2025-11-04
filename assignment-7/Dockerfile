FROM python:3.11.14-slim

WORKDIR /app

COPY app.py /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5056

CMD ["python3", "app.py"]