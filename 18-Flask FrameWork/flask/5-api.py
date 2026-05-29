## Put and Delete HTTP Methods in Flask Framework
## Working with API's--json

from flask import Flask, jsonify, request


app = Flask(__name__)


## Initial Data in my todo list
my_items = [
    { "id": 1, "name": "Buy Groceries", "status": "pending" },
    { "id": 2, "name": "Clean the House", "status": "in-progress" },
    { "id": 3, "name": "Finish Homework", "status": "completed" },
    { "id": 4, "name": "Go for a Walk", "status": "pending" }
]


@app.route('/')
def home():
    return "Welcome to the Todo List API!"


## GET : Retrieve all items in the todo list
@app.route('/items')
def items():
    return jsonify(my_items)  



## GET: Retrieve a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in my_items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


## POST : Create a new Task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Name is required"}), 400
    new_item = {
        "id": my_items[-1]['id'] + 1 if my_items else 1,
        "name": request.json['name'],
        "status": request.json['status'] if 'status' in request.json else 'pending'
    }
    my_items.append(new_item)
    return jsonify(new_item), 201

## PUT : Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in my_items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404
    else:
        item['name'] = request.json.get('name', item['name'])
        item['status'] = request.json.get('status', item['status'])
        return jsonify(item), 200

## Delete : Remove an item from the list
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # item = next((item for item in items if item['id'] == item_id), None)
    # if item is None:
    #     return jsonify({"error": "Item not found"}), 404
    # else:
    #     items.remove(item)
    #     return jsonify({"message": "Item deleted successfully"}), 200

    global my_items
    my_items = [item for item in my_items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200





if __name__ == '__main__':
    app.run(debug=True)