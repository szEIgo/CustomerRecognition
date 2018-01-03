import json
from flask import Flask, request

import sys

sys.path.insert(0, '../')

import config as cfg
from producer_task.KQProducer import kproducer
from producer_task.producer import producer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def produceBoth():
    data = request.get_json()
    json_data = json.dumps(data)
    print("Recevied post    : ", json_data)
    producer.produceQueue(json_data)

    kproducer.produceQueue(str(cfg.QUEUE_TOPIC), json_data)

    return "Rabbit & Kafka"


@app.route('/rabbit', methods=['POST'])
def produceRabbit():
    data = request.get_json()
    json_data = json.dumps(data)
    print("Recevied post: ", json_data)
    producer.produceQueue(json_data)
    return "Rabbit MSG produced"


@app.route('/kafka', methods=['POST'])
def produceKafka():
    data = request.get_json()
    json_data = json.dumps(data)
    print("Recevied post: ", json_data)
    kproducer.produceQueue(str(cfg.QUEUE_TOPIC), json_data)
    return "Kafka MSG produced"


@app.route('/stream', methods=['POST'])
def produceKafkaStream():
    data = request.get_json()
    json_data = json.dumps(data)
    print("Recevied post: ", json_data)
    kproducer.kafkaStream(str(cfg.QUEUE_TOPIC), json_data)

    return "Kafka Stream Initiated"


@app.route('/close/', methods=['GET'])
def close():
    producer.closeConnection()
    return "Connection to RabbitMQ was closed"


if __name__ == '__main__':
    app.run(
        debug=True,
        host=cfg.host_ip,
        port=cfg.host_port
    )
