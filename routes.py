from flask import Flask, render_template, request, jsonify
from app import app, db
from models import Item

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = {"id": len(data) + 1, "name": request.json["name"]}
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    new_name = request.json.get("name")
    if new_name:
        item["name"] = new_name
        return jsonify(item)

    return jsonify({"error": "Name field is required"}), 400

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
    return '', 204


@app.route('/api/items/fromdb', methods=['GET'])
def get_items_from_db():
    items = Item.query.all()
    serialized_items = [{"id": item.id, "name": item.name} for item in items]
    return jsonify(serialized_items)

@app.route('/api/items/fromdb', methods=['POST'])
def add_item_to_db():
    new_item = Item(name=request.json["name"])  # Create a new Item instance
    db.session.add(new_item)  # Add the item to the session
    db.session.commit()  # Commit the changes to the database
    return jsonify(new_item), 201

@app.route('/api/items/fromdb/<int:item_id>', methods=['PUT'])
def update_item_in_db(item_id):
    item = Item.query.get(item_id)  # Retrieve the item from the database
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    new_name = request.json.get("name")
    if new_name:
        item["name"] = new_name
        return jsonify(item)

    return jsonify({"error": "Name field is required"}), 400