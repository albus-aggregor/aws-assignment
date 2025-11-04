FROM python:3.10-slim

WORKDIR /app
COPY assignment-4/requirements.txt .
COPY assignment-4/app.py .
RUN pip install -r requirements.txt


CMD ["python3", "app.py"]
