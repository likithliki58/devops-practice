import logging

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return "Hello from DevOps!"


@app.route("/health")
def health():
    logger.info("Health check accessed")
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler("/root/devops-practice/monitoring/logs/app.log"),
        logging.StreamHandler()
    ]
)
