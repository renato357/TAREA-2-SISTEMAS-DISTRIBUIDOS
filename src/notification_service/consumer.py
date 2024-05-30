from kafka import KafkaConsumer
import json
import smtplib
from email.mime.text import MIMEText
import logging  # Importamos logging

from config import KAFKA_BROKER_URL, PROCESSED_TOPIC, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL

consumer = KafkaConsumer(
    PROCESSED_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Definir order_status globalmente
order_status = {}

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())

def consume_notifications():
    global order_status  # Asegurar que estamos actualizando el diccionario global
    for message in consumer:
        order = message.value
        order_id = order['id']
        order_status[order_id] = order
        email_body = f"Order {order_id} is now {order['estado']}."
        send_email(order['email'], 'Order Status Update', email_body)
        logging.info(f"Sent notification for order {order_id} to {order['email']}")  # Agregamos un registro de depuración
