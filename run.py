import logging
import logstash
import socket
from flask import request
from app import create_app

app = create_app()

# Налаштування логера для Logstash
host = 'logstash'  # якщо запускаєш у Docker мережі, інакше 'localhost'
port = 5000

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))

test_logger.info('Flask app started')

# Логування кожного HTTP-запиту
@app.before_request
def log_request():
    test_logger.info({
        'method': request.method,
        'path': request.path,
        'remote_addr': request.remote_addr
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

