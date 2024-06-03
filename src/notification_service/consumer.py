from kafka import KafkaConsumer, KafkaProducer
import json
import time
import smtplib
from email.mime.text import MIMEText
import logging

from config import KAFKA_BROKER_URL, PROCESSED_TOPIC, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL

# Configuración del logging para escribir un archivo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("/app/logs/notification_service.log"),
        logging.StreamHandler()
    ]
)

consumer = KafkaConsumer(
    PROCESSED_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    group_id='notification_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

order_status = {}

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def consume_notifications():
    global order_status
    for message in consumer:
        start_time = time.time()
        try:
            order = message.value
            order_id = order['id']
            order_status[order_id] = order
            email_body = f"Order {order_id} is now {order['estado']}."
            send_email(order['email'], 'Order Status Update', email_body)
        except Exception as e:
            logging.error(f"Error processing Order notification: {e}")
        end_time = time.time()
        logging.info(f"Order Notification {order_id}. Processed notification in {end_time - start_time} seconds to {order['email']}")
 