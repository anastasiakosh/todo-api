import logging
import json
import socket
from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

# Налаштування TCP логера
class TCPLogHandler(logging.Handler):
    def emit(self, record):
        try:
            log_entry = self.format(record)
            sock = socket.create_connection(("logstash", 5000))
            sock.sendall(log_entry.encode('utf-8') + b'\n')
            sock.close()
        except Exception:
            pass  # або log в stderr

logger = logging.getLogger('flask_app')
logger.setLevel(logging.INFO)

tcp_handler = TCPLogHandler()
tcp_handler.setFormatter(logging.Formatter(json.dumps({
    "level": "%(levelname)s",
    "message": "%(message)s",
    "time": "%(asctime)s",
    "module": "%(module)s"
})))
logger.addHandler(tcp_handler)

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    logger.info("Index endpoint hit")
    return "Hello from Flask!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

