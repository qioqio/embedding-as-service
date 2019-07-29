'''Server.py'''

import json
import argparse
import numpy as np
import tqdm
from socket import *
from gensim.models.keyedvectors import KeyedVectors

parser = argparse.ArgumentParser()
parser.add_argument("--local_rank", type=int)
args = parser.parse_args()

HOST = gethostname()
PORT = 2333
BUFFSIZE = 2048


def load_txt_raw(
        fn=r'Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt',
        dtype='float16'):
    """
    Load the word2vec dict from raw txt file.
    Dict key is word and value is a np.ndarray of vector.
    :param fn: File name of the raw data file
    :param dtype: dtype of the vector array,
                default float16 is enough since the round of digit in the array is less than 5
    :return: dict of word2vec model
    """
    ret = []
    with open(fn, 'r', encoding='utf-8') as fin:
        fin.readline()
        for line in fin:
            ret.append(list(line.split(' ')))
            del line
    ret = {
        x[0]: np.array([float(_) for _ in x[1:]], dtype=dtype)
        for x in ret[1:]
    }
    return ret


dict = KeyedVectors.load_word2vec_format(
    r'Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt',
    binary=False)

# dict = {'hello': [1.0, 25, 5]}
ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)
print('Server start at: %s:%s' %(HOST, PORT))

while True:
    print("waiting for connection")
    tcpClient, addr = tcpServer.accept()
    print("--connect from ", addr)
    while True:
        data = tcpClient.recv(BUFFSIZE).decode()
        if not data:
            print("close connect    ")
            break
        # print(dict)
        # print(data)
        try:
            embedding = dict['computer']
        except :
            embedding = [0 for i in range(300)]
        else:
            embedding = [0 for i in range(300)]
        json_string = json.dumps(embedding)
        # print(json_string)
        tcpClient.send(json_string.encode())
        # print()

tcpServer.close()
tcpClient.close()
