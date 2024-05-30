import unittest
from src.processing_service.consumer import process_order

class TestProcessingService(unittest.TestCase):
    def test_process_order(self):
        order = {'id': '123', 'name': 'Test Order', 'price': 10.99, 'email': 'test@example.com'}
        process_order(order)
        self.assertEqual(order['estado'], 'finalizado')

if __name__ == '__main__':
    unittest.main()
