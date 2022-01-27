import unittest
import requests
import json

class Testmain(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"
    def test_add_item(self):
        url = f'{self.base_url}/items/add'
        data = {"item": "test3454"}
        res = requests.post(url, json=data)
        self.assertEqual(res.status_code, 201)
    
    def test_get_all_items(self):
        url = f'{self.base_url}/items/all'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_item(self):
        url = f'{self.base_url}/item/status'
        data = {"name": "Hello23"}
        res = requests.get(url, params=data)
        self.assertEqual(res.status_code, 200)

    def test_update_status(self):
        url = f'{self.base_url}/item/update'
        data = {"item": "test", "status": "completed"}
        res = requests.put(url, json=data)
        self.assertEqual(res.status_code, 200)

    def test_delete_item(self):
        url = f'{self.base_url}/item/remove'
        data = {"item": "test"}
        res = requests.delete(url, json=data)
        self.assertEqual(res.status_code, 204)

if __name__ == '__main__':
    unittest.main()
