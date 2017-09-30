import requests

class Client(object):
    def __init__(self):
        self.s = requests.session()
