import json
import sys
import socket
from socket import *


class WebEmbedding():
    def __init__(self):
        self.HOST = gethostname()
        self.PORT = 2333
        self.BUFFSIZE = 2048
        self.ADDR = (self.HOST, self.PORT)
        self.tcpClient = socket(AF_INET, SOCK_STREAM)
        self.tcpClient.connect(self.ADDR)

    def get_embedding(self, word):
        self.tcpClient.send(word)
        json_string = self.tcpClient.recv(self.BUFFSIZE)
        if not json_string:
            sys.exit()
        embedding = json.loads(json_string.decode())
        return embedding

    def close(self):
        self.tcpClient.close()


web = WebEmbedding()
words = ['x', 'hello']

for word in words:
    word = word.encode()
    embedding = web.get_embedding(word)
    print(embedding)
    print(type(embedding[0]))

web.close()
