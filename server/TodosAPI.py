from flask import Blueprint, jsonify, request

todos_api = Blueprint('todos_api', __name__)

todos = ['Study Python', 'Study JavaScript', 'Clean Room']

@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    return jsonify({todos})
