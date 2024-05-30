from flask import Flask, request, jsonify
from producer import produce_request

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    if 'name' not in data or 'price' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    order_id = produce_request(data)
    return jsonify({'order_id': order_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
