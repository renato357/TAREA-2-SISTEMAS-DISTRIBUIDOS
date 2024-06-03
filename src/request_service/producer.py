# producer.py
from kafka import KafkaProducer
import json
import uuid
from config import KAFKA_BROKER_URL, ORDER_TOPIC
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("/app/logs/request_service.log"),
        logging.StreamHandler()
    ]
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

from kafka.errors import KafkaError

def produce_request(data):
    order_id = str(uuid.uuid4())
    data['id'] = order_id
    try:
        producer.send(ORDER_TOPIC, data).add_errback(on_send_error)
        producer.flush()
        logging.info(f"Order {order_id} sent to topic {ORDER_TOPIC}")
    except KafkaError as e:
        logging.error(f"Failed to send message: {e}")
    return order_id

def on_send_error(excp):
    logging.error('Error while sending message', exc_info=excp)
