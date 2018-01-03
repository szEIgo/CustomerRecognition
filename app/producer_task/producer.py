import pika

import sys
sys.path.insert(0,'../')

import config as cfg


class producer:

    credentials = pika.PlainCredentials(cfg.RABBIT_USER, cfg.RABBIT_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(str(cfg.RABBIT_HOST), int(cfg.RABBIT_PORT), '/',  credentials))

    channel.queue_declare(queue=cfg.QUEUE_TOPIC)
    print("we are here!")

    def produceQueue(message):
        channel = producer.connection.channel()
        channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
        print("Send  RMQ  Queue : ", message)

    def closeConnection(self):
        producer.connection.close()
