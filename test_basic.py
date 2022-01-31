import unittest
from main import app

base_url = "http://127.0.0.1:5000"

class TestTodoList(unittest.TestCase):
    """Testing the Flask APIs using unittest"""
    def test_add_item(self):
        # Add item to the list
        data = {"item": "Test Item5"}
        response = app.test_client().post(base_url + "/item/add", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, "application/json")

    def test_get_items(self):
        # Get all items
        response = app.test_client().get(base_url + "/items/all")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_update_item(self):
        # Update item
        data = {"item": "Test Item5", "status": "Completed"}
        response = app.test_client().put(base_url + "/item/update", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_delete_item(self):
        # Delete item
        data = {"item": "Test Item5"}
        response = app.test_client().delete(base_url + "/item/delete", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        
if __name__ == '__main__':
    unittest.main()
