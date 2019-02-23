#!/usr/bin/env python

import glob
import sys
import datetime

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import PaymentAuthorization, PaymentAuthorizationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19096)

class PaymentAuthorizationHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def createConnection(self, port, server):
      transport = TSocket.TSocket('localhost', port)
      transport = TTransport.TBufferedTransport(transport)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      client = server.Client(protocol)
      transport.open()
      return client, transport


    def authorize(self, cardNumber, amount):
      clientAuthRuleDB, protocolAuthRuleDB = self.createConnection(19098, PaymentAuthorizationDB)
      limit = clientAuthRuleDB.getLimit(cardNumber)
      protocolAuthRuleDB.close()
      if amount <= limit: return True
      else: return False

    def changeAuthRule(self, cardNumber, newAmount):
      clientAuthRuleDB, protocolAuthRuleDB = self.createConnection(19098, PaymentAuthorizationDB)
      ack = clientAuthRuleDB.changeLimit(cardNumber, newAmount)
      protocolAuthRuleDB.close()
      return ack

if __name__ == '__main__':
    handler = PaymentAuthorizationHandler()
    processor = PaymentAuthorization.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the PaymentAuthorizationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' PaymentAuthorizationServer done.')
