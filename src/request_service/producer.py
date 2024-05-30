from kafka import KafkaProducer
import json
import uuid
from config import KAFKA_BROKER_URL, ORDER_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_request(data):
    order_id = str(uuid.uuid4())
    data['id'] = order_id
    producer.send(ORDER_TOPIC, data)
    producer.flush()
    return order_id
