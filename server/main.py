from flask import Flask, render_template, jsonify
from app import create_app

def add_vue_routes(app):
    @app.route('/')
    def serve_vue_app():
        """
        Server our vue app
        """
        return(render_template('index.html'))

    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers["Cache-Control"] = "no-cache"
        return req

    todos = ['Study Python', 'Study JavaScript', 'Clean Room']

    @app.route('/todos', methods=['GET'])
    def serve_all_todos():
        return jsonify({"items": todos})


if __name__ == "__main__":
    app = create_app()
    add_vue_routes(app)
    app.run(debug=True)
