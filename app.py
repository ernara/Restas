from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # SQLite database file
db = SQLAlchemy(app)

# Create a model for the items table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    data = [{"id": item.id, "name": item.name} for item in items]
    return jsonify(data)

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item_name = request.json.get("name")
    if new_item_name:
        new_item = Item(name=new_item_name)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"id": new_item.id, "name": new_item.name}), 201
    return jsonify({"error": "Name field is required"}), 400

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if item:
        new_name = request.json.get("name")
        if new_name:
            item.name = new_name
            db.session.commit()
            return jsonify({"id": item.id, "name": item.name})
        return jsonify({"error": "Name field is required"}), 400
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True)
