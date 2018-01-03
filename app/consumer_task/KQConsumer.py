from kafka import KafkaConsumer

import sys

sys.path.insert(0, '../')

import config as cfg


def consumer():
    bootstrap = cfg.KAFKA_HOST + ':' + cfg.KAFKA_PORT
    KQConsumer = KafkaConsumer(bootstrap_servers=str(bootstrap),
                               auto_offset_reset='earliest')
    KQConsumer.subscribe([cfg.QUEUE_TOPIC])
    print("listening for publishers")
    for message in KQConsumer:
        print(message)

consumer()

