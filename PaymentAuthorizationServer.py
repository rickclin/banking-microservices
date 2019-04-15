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

SERVER_PORT = ('0.0.0.0', 9090)

class PaymentAuthorizationHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def createConnection(self, container, server):
      transport = TSocket.TSocket(container, 9090)
      transport = TTransport.TFramedTransport(transport)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      client = server.Client(protocol)
      transport.open()
      return client, transport


    def authorize(self, cardNumber, amount):
      clientAuthRuleDB, protocolAuthRuleDB = self.createConnection('payment-authorization-db', PaymentAuthorizationDB)
      limit = clientAuthRuleDB.getLimit(cardNumber)
      protocolAuthRuleDB.close()
      if amount <= limit: return True
      else: return False

    def changeAuthRule(self, cardNumber, newAmount):
      clientAuthRuleDB, protocolAuthRuleDB = self.createConnection('payment-authorization-db', PaymentAuthorizationDB)
      ack = clientAuthRuleDB.changeLimit(cardNumber, newAmount)
      protocolAuthRuleDB.close()
      return ack

if __name__ == '__main__':
    handler = PaymentAuthorizationHandler()
    processor = PaymentAuthorization.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the PaymentAuthorizationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' PaymentAuthorizationServer done.')
