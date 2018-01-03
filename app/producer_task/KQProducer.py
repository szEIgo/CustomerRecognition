from kafka import KafkaProducer, SimpleProducer, KafkaClient
import threading, time, sys

sys.path.insert(0, './')

import config as cfg
import sys


class kproducer(threading.Thread):
    daemon = True
    bootstrap = cfg.KAFKA_HOST + ':' + cfg.KAFKA_PORT

    def produceQueue(topic, message):
        producer = KafkaProducer(bootstrap_servers=kproducer.bootstrap)
        producer.send(topic, str.encode(message))
        print("Send Kafka Queue : ", message)
        producer.close()

    def kafkaStream(topic, message):
        producer = KafkaProducer(bootstrap_servers=kproducer.bootstrap)

        def acked(err, msg):
            if err is not None:
                print("Failed to deliver message: {0}: {1}"
                      .format(msg.value(), err.str()))
            else:
                print("Message produced: {0}".format(msg.value()))

        try:
            for val in range(1, 1000):
                producer.send(topic, str.encode('#{0}'.format(val) + str.encode(message).decode('utf-8')))
                print("Send Kafka Queue : " + '#{0}'.format(val) + message)
                time.sleep(0.2)

        except KeyboardInterrupt:
            pass

        producer.flush(30)
        producer.close()
