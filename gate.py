import urllib.request
import urllib.parse
import base64
import sys

class Gate:
    """class for using iqsms.ru service via GET requests"""
    """modified to python 3.6 support by Fisiks (github)"""
    
    __host = 'gate.iqsms.ru'
    
    def __init__(self, api_login, api_password):
        self.login = api_login
        self.password = api_password
    
    def __sendRequest(self, uri, params=None):
        url = self.__getUrl(uri, params)
        request = urllib.request.Request(url)
        passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, self.login, self.password)
        authhandler = urllib.request.HTTPBasicAuthHandler(passman)
        try:
            opener = urllib.request.build_opener(authhandler)
            data = opener.open(request).read()
            return data
        except IOError as e:
            return e.code
        
    def __getUrl(self, uri, params=None):
        url = "http://%s/%s/" % (self.getHost(), uri)
        paramStr = ''
        normalisedPatams = dict()
        if params is not None:
            for k, v in params.items():
                if v is not None: 
                    normalisedPatams[k] = v
            normalisedPatams = urllib.parse.urlencode(params)
        return "%s?%s" % (url, normalisedPatams)
    
    def getHost(self):
        """Return current requests host """
        return self.__host
        
    def setHost(self, host):
        """Changing default requests host """
        self.__host = host
                
    def send(self, phone, text, sender='iqsms', 
             statusQueueName=None, scheduleTime=None, wapurl = None):
        """Sending sms """
        params = {
                  'phone': phone, 
                  'text': text, 
                  'sender': sender,
                  'statusQueueName': statusQueueName,
                  'scheduleTime': scheduleTime, 
                  'wapurl': wapurl
                 }
        return self.__sendRequest('send', params)
    
    def status(self, id):
        """Retrieve sms status by it's id """
        params = {'id': id}
        return self.__sendRequest('status', params)
    
    def statusQueue(self, statusQueueName, limit = 5):
        """Retrieve latest statuses from queue """
        params = {'statusQueueName': statusQueueName, 'limit': limit}
        return self.__sendRequest('statusQueue', params)
    
    def credits(self):
        """Retrieve current credit balance """
        return self.__sendRequest('credits')
    
    def senders(self):
        """Retrieve available signs """
        return self.__sendRequest('senders')
    
    
    
if __name__ == "__main__":
    print (Gate.__doc__)