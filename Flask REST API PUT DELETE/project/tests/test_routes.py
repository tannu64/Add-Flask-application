import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_items(self):
        """Test fetching all items."""
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_put_item(self):
        """Test adding/updating an item."""
        response = self.client.put('/items/1', json={'name': 'Test Item'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Item', response.get_json()['item']['1'])

    def test_delete_item(self):
        """Test deleting an item."""
        self.client.put('/items/1', json={'name': 'Test Item'})
        response = self.client.delete('/items/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

