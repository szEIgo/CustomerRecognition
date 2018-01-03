import os

########################################
if os.getenv("queue-topic"):
    QUEUE_TOPIC = os.environ.get("queue-topic")
else:
    QUEUE_TOPIC = "test"
########################################
if os.getenv("rabbit-ip"):
    RABBIT_HOST = os.environ.get("rabbit-ip")
else:
    RABBIT_HOST = "172.17.0.1"
if os.getenv("rabbit-port"):
    RABBIT_PORT = int(os.environ.get("rabbit-port"))
else:
    RABBIT_PORT = 5672
if os.getenv("rabbit-user"):
    RABBIT_USER = str(os.environ.get("rabbit-user"))
else:
    RABBIT_USER = "user"
if os.getenv("rabbit-password"):
    RABBIT_PASSWORD = str(os.environ.get("rabbit-password"))
else:
    RABBIT_PASSWORD = "bitnami"
########################################
if os.getenv("kafka-ip"):
    KAFKA_HOST = os.environ.get("kafka-ip")
else:
    KAFKA_HOST = "172.17.0.1"
if os.getenv("kafka-port"):
    KAFKA_PORT = os.environ.get("kafka-port")
else:
    KAFKA_PORT = "9092"
########################################
if os.getenv("WEBSERVER_IP"):
    host_ip = os.environ.get("WEBSERVER_IP")
else:
    host_ip = "172.17.0.1"
if os.getenv("WEBSERVER_PORT"):
    host_port = os.environ.get("WEBSERVER_PORT")
else:
    host_port = 5000
########################################

    print("flask ip:", host_ip)
    print("kafka ip:", KAFKA_HOST)
    print("kafka port:", KAFKA_PORT)
    print("rabbit ip:", RABBIT_HOST)
    print("rabbit port:",RABBIT_PORT)
    print("topic:", QUEUE_TOPIC)