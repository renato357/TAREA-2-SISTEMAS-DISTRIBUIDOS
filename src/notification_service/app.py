from consumer import consume_notifications, order_status
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status/<order_id>', methods=['GET'])
def status(order_id):
    if order_id not in order_status:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order_status[order_id])

if __name__ == '__main__':
    from threading import Thread
    Thread(target=consume_notifications).start()
    app.run(host='0.0.0.0', port=5001)
