from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (replace this with your database or data storage)
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    # Add more data as needed
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

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
