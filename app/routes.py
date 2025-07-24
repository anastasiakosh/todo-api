from flask import Blueprint, jsonify, request
from prometheus_client import Counter

todo_bp = Blueprint('todo', __name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

from .models import todos

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    REQUEST_COUNT.inc()
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    REQUEST_COUNT.inc()
    data = request.get_json()
    todos.append(data)
    return jsonify(data), 201

