import os

if os.getenv("WEBSERVER_IP"):
    host_ip = os.environ.get("WEBSERVER_IP")
else:
    host_ip = "0.0.0.0"
    
if os.getenv("WEBSERVER_PORT"):
    host_port = os.environ.get("WEBSERVER_PORT")
else:
    host_port = 5000
