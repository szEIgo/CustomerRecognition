import requests as r
import unittest
import json
from flaskConnection import FConnection as flask
import config as cfg


class TestFlask(unittest.TestCase):
    URL = 'http://' + str(cfg.host_ip) + ':' + str(cfg.host_port)
    print(URL)

    def test_valid_url_length(self):
        self.assertTrue(flask.valid_url_name(TestFlask.URL))

    def test_postReq(self):
        msg_json = {'is_claimed': 'True', 'rating': 3.5}
        self.assertEqual(flask.postRequest(r, json.dumps(msg_json), TestFlask.URL), "rabbit")

    def test_getReq(self):
        self.assertEqual(flask.getRequest(r, TestFlask.URL), "<Response [405]>")


if __name__ == '__main__':
    unittest.main()
