import json
import pika

import sys
sys.path.insert(0,'../')

import config as cfg


class consume():
    credentials = pika.PlainCredentials(cfg.RABBIT_USER, cfg.RABBIT_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("172.17.0.1", cfg.RABBIT_PORT, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue=cfg.QUEUE_TOPIC)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def observer():
        def callback(ch, method, properties, body):
            print("Method: {}".format(method))
            print("Properties: {}".format(properties))
            data = json.loads(body.decode('utf-8'))
            print("Name: {}".format(data['name']))
            print("Email: {}".format(data['email']))

        consume.channel.basic_consume(callback,
                                      queue=cfg.QUEUE_TOPIC, no_ack=True)
        consume.channel.start_consuming()


consume.observer()
