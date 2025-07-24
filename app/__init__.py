from flask import Flask
from .routes import todo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    return app

