class FConnection():
    def valid_url_name(self):
        if len(str(self)) > 12:
            return True
        else:
            return False

    def postRequest(self, messageDict, URL):
        dictToSend = messageDict
        res = self.post(URL, json=dictToSend)
        return res.text

    def getRequest(self, URL):
        res = self.get(URL)
        return str(res)
