from tests.base import BaseTestCase
import json


class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')
