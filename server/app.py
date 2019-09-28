import os
from flask import Flask, render_template
from TodosAPI import todos_api

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.register_blueprint(todos_api)
    return app

