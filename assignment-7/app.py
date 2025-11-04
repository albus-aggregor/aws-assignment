from flask import Flask, jsonify
import random
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

@app.route('/')
def home():
    app.logger.info("Home endpoint hit")
    if random.choice([True, False]):
        app.logger.error("Random failure occurred")
        raise Exception("Simulated random failure!")
    return jsonify({"message": "App is working fine"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5056)
