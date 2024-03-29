from flask import render_template, request, jsonify
from app import app, db
from models.item import Item

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items/fromdb', methods=['GET'])
def get_items():
    items = Item.query.all()
    serialized_items = [{"id": item.id, "name": item.name} for item in items]
    return jsonify(serialized_items)


@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = Item(name=request.json["name"]) 
    db.session.add(new_item) 
    db.session.commit()
    return jsonify(new_item.serialize()), 201

@app.route('/api/items/fromdb/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    new_name = request.json.get("name")
    if new_name:
        item.name = new_name 
        db.session.commit()  
        return jsonify(item.serialize())

    return jsonify({"error": "Name field is required"}), 400


@app.route('/api/items/fromdb/<int:item_id>', methods=['DELETE'])
def delete_item_from_db(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    db.session.delete(item)
    db.session.commit()
    return '', 204

