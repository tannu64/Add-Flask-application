import uuid

# In-memory data store
class ItemModel:
    def __init__(self):
        # Use a dictionary to store items with unique IDs as keys
        self.items = {}

    def get_all_items(self):
        """Return all items."""
        return self.items

    def get_item(self, item_id):
        """Return a single item by ID."""
        return self.items.get(item_id)

    def add_or_update_item(self, item_id, name):
        """Add or update an item."""
        self.items[item_id] = {'id': item_id, 'name': name}
        return self.items[item_id]

    def delete_item(self, item_id):
        """Delete an item by ID."""
        return self.items.pop(item_id, None)

# Instantiate the model to use in the application
item_model = ItemModel()

