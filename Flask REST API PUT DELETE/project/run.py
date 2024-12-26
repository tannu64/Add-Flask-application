from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# In-memory data store for demonstration
items = {}

# Route to render HTML page with buttons and features
@app.route('/')
def index():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Single Page</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .container { width: 50%; margin: auto; text-align: center; padding: 20px; }
            .button { padding: 10px 20px; margin: 10px; border: none; border-radius: 5px; cursor: pointer; }
            .button-add { background-color: green; color: white; }
            .button-update { background-color: blue; color: white; }
            .button-delete { background-color: red; color: white; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Manage Items</h1>
            <form id="addForm">
                <input type="text" id="itemName" placeholder="Enter item name" required>
                <button type="button" class="button button-add" onclick="addItem()">Add Item</button>
            </form>
            <div id="itemsList">
                <h3>Items List:</h3>
                <ul id="items"></ul>
            </div>
        </div>
        <script>
            async function fetchItems() {
                const response = await fetch('/items');
                const data = await response.json();
                const itemsList = document.getElementById('items');
                itemsList.innerHTML = '';
                for (const [key, value] of Object.entries(data)) {
                    itemsList.innerHTML += `<li>${value} 
                        <button class="button button-update" onclick="updateItem('${key}')">Update</button>
                        <button class="button button-delete" onclick="deleteItem('${key}')">Delete</button>
                    </li>`;
                }
            }

            async function addItem() {
                const itemName = document.getElementById('itemName').value;
                const itemId = new Date().getTime().toString(); // Generate a unique ID
                if (itemName) {
                    await fetch(`/items/${itemId}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name: itemName }),
                    });
                    fetchItems();
                }
            }

            async function updateItem(itemId) {
                const newName = prompt("Enter new name for the item:");
                if (newName) {
                    await fetch(`/items/${itemId}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name: newName }),
                    });
                    fetchItems();
                }
            }

            async function deleteItem(itemId) {
                await fetch(`/items/${itemId}`, { method: 'DELETE' });
                fetchItems();
            }

            fetchItems(); // Load items when the page loads
        </script>
    </body>
    </html>
    """
    return render_template_string(html_code)

# RESTful API endpoints
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<item_id>', methods=['PUT'])
def put_item(item_id):
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    items[item_id] = data['name']
    return jsonify({'message': 'Item added/updated', 'item': {item_id: data['name']}}), 201

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404
    deleted_item = items.pop(item_id)
    return jsonify({'message': 'Item deleted', 'item': deleted_item})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
