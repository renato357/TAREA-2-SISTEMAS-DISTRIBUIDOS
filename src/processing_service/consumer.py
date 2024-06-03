from kafka import KafkaConsumer, KafkaProducer
import json
import time
from time import sleep
import logging

from config import KAFKA_BROKER_URL, ORDER_TOPIC, PROCESSED_TOPIC

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("/app/logs/processing_service.log"),
        logging.StreamHandler()
    ]
)

consumer = KafkaConsumer(
    ORDER_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    group_id='processing_group',  # Grupo de consumidores
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def process_order(order):
    states = ['recibido', 'preparando', 'entregando', 'finalizado']
    for state in states:
        order['estado'] = state
        producer.send(PROCESSED_TOPIC, order)
        producer.flush()
        sleep(0.05)  # Simula el tiempo de procesamiento
        logging.info(f"Processed order {order['id']} with state {state}")  # Agregamos un registro de depuración

def consume_requests():
    for message in consumer:
        start_time = time.time()
        try:
            order = message.value
            process_order(order)
        except Exception as e:
            logging.error(f"Error processing order: {e}")
        end_time = time.time()
        logging.info(f"Processed in {end_time - start_time} seconds order {order['id']}")
