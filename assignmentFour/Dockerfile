FROM python:3.10-slim

WORKDIR /app
COPY assignmentFour/requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "app.py"]
