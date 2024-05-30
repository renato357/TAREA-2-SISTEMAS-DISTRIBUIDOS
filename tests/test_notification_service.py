import unittest
from src.notification_service.consumer import send_email

class TestNotificationService(unittest.TestCase):
    def test_send_email(self):
        send_email('test@example.com', 'Test Subject', 'Test Body')

if __name__ == '__main__':
    unittest.main()
