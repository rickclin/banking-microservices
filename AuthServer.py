#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift import Thrift
from bank import AuthenticateService
from hashlib import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

SERVER_PORT = ('0.0.0.0', 9090)

user_db = {'ricklin' : '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',
           'user'    : 'c73ba2982c55b7ead0e4098a92f722bdb3a3b3d8'
          }

class AuthenticateHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def authenticate(self, user, password):
        digest = sha1(password.encode('utf-8')).hexdigest()
        if user in user_db.keys():
          return user_db[user] == digest
        else:
          return False

if __name__ == '__main__':
    handler = AuthenticateHandler()
    processor = AuthenticateService.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the AuthServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] AuthServer done.')
