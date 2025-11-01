FROM python:3.9.24-slim

WORKDIR /app

COPY . .

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python3", "app.py"]
