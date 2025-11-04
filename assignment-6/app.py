from flask import Flask, jsonify, request
from prometheus_client import (
    Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
)
import time
import random

app = Flask(__name__)

# ------------------------
# 📊 METRICS DEFINITIONS
# ------------------------

# Count total requests grouped by method & endpoint
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests (grouped by method, endpoint, and status)",
    ["method", "endpoint", "status"]
)

# Measure request latency
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency in seconds (grouped by endpoint)",
    ["endpoint"]
)

# Track application business metrics
ACTIVE_USERS = Gauge(
    "active_users",
    "Number of active users currently connected"
)

ORDER_VALUE = Histogram(
    "order_value_dollars",
    "Order values processed by the system (in USD)"
)


# ------------------------
# 🧠 ENDPOINTS
# ------------------------

@app.route("/")
def home():
    start = time.time()
    try:
        REQUEST_COUNT.labels(method="GET", endpoint="/", status="200").inc()
        ACTIVE_USERS.inc(random.randint(0, 3))  # simulate users
        time.sleep(random.uniform(0.1, 0.5))  # simulate latency
        REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start)
        return jsonify({"message": "Welcome to Prometheus Dashboard App!"})
    finally:
        ACTIVE_USERS.dec(random.randint(0, 2))  # simulate logout


@app.route("/order", methods=["POST"])
def create_order():
    start = time.time()
    try:
        value = random.uniform(10, 500)
        ORDER_VALUE.observe(value)
        REQUEST_COUNT.labels(method="POST", endpoint="/order", status="201").inc()
        time.sleep(random.uniform(0.2, 0.8))
        REQUEST_LATENCY.labels(endpoint="/order").observe(time.time() - start)
        return jsonify({"status": "success", "order_value": value}), 201
    except Exception:
        REQUEST_COUNT.labels(method="POST", endpoint="/order", status="500").inc()
        return jsonify({"status": "error"}), 500


@app.route("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health", status="200").inc()
    return jsonify({"status": "healthy"})


@app.route("/metrics")
def metrics():
    """Expose Prometheus metrics endpoint"""
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


# ------------------------
# ▶️ RUN APP
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055)
