#!/usr/bin/env python

import glob
import sys
import datetime

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import PaymentAuthorizationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19098)
AUTHORIZATION_RULE = {'cardNumber': 'limit', '0000000000000000': 50.00}

class PaymentAuthorizationDBHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def getLimit(self, cardNumber):
      global AUTHORIZATION_RULE
      if cardNumber in AUTHORIZATION_RULE:
        return float(AUTHORIZATION_RULE[cardNumber])
      else:
        return 0.00

    def changeLimit(self, cardNumber, newAmount):
      global AUTHORIZATION_RULE
      if cardNumber in AUTHORIZATION_RULE:
        AUTHORIZATION_RULE[cardNumber] = float(newAmount)
        return True
      else:
        return False
    
    def addLimit(self, cardNumber, amount):
      if cardNumber in AUTHORIZATION_RULE:
        return False

      AUTHORIZATION_RULE[cardNumber] = amount
      return True

if __name__ == '__main__':
    handler = PaymentAuthorizationDBHandler()
    processor = PaymentAuthorizationDB.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the PaymentAuthorizationDBServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' PaymentAuthorizationDBServer done.')
