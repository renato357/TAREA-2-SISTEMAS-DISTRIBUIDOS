import unittest
from src.request_service.app import app

class TestRequestService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_order(self):
        response = self.app.post('/order', json={
            'name': 'Test Order',
            'price': 10.99,
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('order_id', response.json)

if __name__ == '__main__':
    unittest.main()
