from flask import Blueprint, request, jsonify
from app.models import item_model

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/items', methods=['GET'])
def get_items():
    return jsonify(item_model.get_all_items())

@api_blueprint.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = item_model.get_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@api_blueprint.route('/items/<item_id>', methods=['PUT'])
def put_item(item_id):
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    item = item_model.add_or_update_item(item_id, data['name'])
    return jsonify({'message': 'Item added/updated', 'item': item}), 201

@api_blueprint.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = item_model.delete_item(item_id)
    if item:
        return jsonify({'message': 'Item deleted', 'item': item})
    return jsonify({'error': 'Item not found'}), 404
