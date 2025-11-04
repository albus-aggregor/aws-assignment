from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    r.incr("hits")
    count = r.get("hits")
    return f"Hello! This page has been viewed {count} times."

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
