import unittest
import requests
import json

# Define the base URL for your API
BASE_URL = 'http://localhost:5000/api'

class TestPersonAPI(unittest.TestCase):

    def setUp(self):
        # Add a person to the database before testing
        data = {
            "_id": "4",
            "name": "Eva Davis",
            "age": 35
        }
        response = requests.post(BASE_URL, json=data)
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        # Remove the added person after testing
        response = requests.delete(f'{BASE_URL}/4')
        self.assertEqual(response.status_code, 200)

    def test_get_person(self):
        # Test fetching details of an existing person
        response = requests.get(f'{BASE_URL}/4')
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        person = json.loads(response.text)
        self.assertEqual(person['_id'], '4')
        self.assertEqual(person['name'], 'Eva Davis')
        self.assertEqual(person['age'], 35)

    def test_update_person(self):
        # Test updating details of an existing person
        updated_data = {
            "age": 36
        }
        response = requests.put(f'{BASE_URL}/4', json=updated_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
