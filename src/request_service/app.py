from flask import Flask, request, jsonify
from producer import produce_request
import json
import os
import logging
from time import sleep


app = Flask(__name__)

# Configuracion del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

@app.route('/order', methods=['POST'])
def order():
   data = request.json
   if 'name' not in data or 'price' not in data or 'email' not in data:
       return jsonify({'error': 'Invalid data'}), 400


   order_id = produce_request(data)
   return jsonify({'order_id': order_id}), 201

#Carga en un instante. Dataset 1
@app.route('/load_dataset_1', methods=['POST'])
def load_dataset_1():
    logging.info("Loading dataset...")
    dataset_path = '1_products_dataset.json'
    if not os.path.exists(dataset_path):
        logging.error(f"File {dataset_path} does not exist.")
        return jsonify({'error': 'Dataset file not found'}), 404
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)
    for data in dataset:
        logging.info(f"Producing request for data: {data}")
        produce_request(data)
    logging.info("Dataset loaded successfully.")
    return jsonify({'status': 'Dataset loaded successfully'}), 200

#Carga con intervalo de tiempo 50ms c/u. Dataset 1
@app.route('/load_dataset_interval_1', methods=['POST'])
def load_dataset_interval_1():
    logging.info("Loading dataset...")
    dataset_path = '1_products_dataset.json'
    if not os.path.exists(dataset_path):
        logging.error(f"File {dataset_path} does not exist.")
        return jsonify({'error': 'Dataset file not found'}), 404
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)
    for data in dataset:
        logging.info(f"Producing request for data: {data}")
        produce_request(data)
        sleep(0.01)  # Intervalo de tiempo de 10 ms
    logging.info("Dataset loaded successfully.")
    return jsonify({'status': 'Dataset loaded successfully'}), 200


@app.route('/load_dataset_2', methods=['POST'])
def load_dataset_2():
    logging.info("Loading dataset...")
    dataset_path = '2_products_dataset.json'
    if not os.path.exists(dataset_path):
        logging.error(f"File {dataset_path} does not exist.")
        return jsonify({'error': 'Dataset file not found'}), 404
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)
    for data in dataset:
        logging.info(f"Producing request for data: {data}")
        produce_request(data)
    logging.info("Dataset loaded successfully.")
    return jsonify({'status': 'Dataset loaded successfully'}), 200

@app.route('/load_dataset_interval_2', methods=['POST'])
def load_dataset_interval_2():
    logging.info("Loading dataset...")
    dataset_path = '2_products_dataset.json'
    if not os.path.exists(dataset_path):
        logging.error(f"File {dataset_path} does not exist.")
        return jsonify({'error': 'Dataset file not found'}), 404
    with open(dataset_path, 'r') as file:
        dataset = json.load(file)
    for data in dataset:
        logging.info(f"Producing request for data: {data}")
        produce_request(data)
        sleep(0.01) # Tiempo de 10 ms
    logging.info("Dataset loaded successfully.")
    return jsonify({'status': 'Dataset loaded successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
