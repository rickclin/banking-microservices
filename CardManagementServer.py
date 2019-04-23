#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import CardManagement, TransactionHistory, PaymentAuthorization

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

import thriftpy2
from thriftpy2.rpc              import make_client
from thriftpy2.protocol.binary  import TBinaryProtocolFactory
from thriftpy2.transport.framed import TFramedTransportFactory
import thrift_connector.connection_pool as connection_pool
bank_thrift = thriftpy2.load("bank.thrift", module_name="bank_thrift")

SERVER_PORT = ('0.0.0.0', 9090)

class CardManagementHandler:
    def __init__(self):
        self.log = {}
        self.TransactionHistoryClient = connection_pool.ClientPool(
          bank_thrift.TransactionHistory,
          'transaction-history', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )
        self.PaymentAuthorizationClient = connection_pool.ClientPool(
          bank_thrift.PaymentAuthorization,
          'payment-authorization', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )

    def ping(self):
        print('ping()')

    def postTransaction(self, cardNumber, description, amount, entryMode):
      # 1. authorize payment
      ack = self.PaymentAuthorizationClient.authorize(cardNumber, amount)
      if ack:
          # 2. insert transaction
          resp = self.TransactionHistoryClient.insertTransaction(cardNumber, amount, entryMode, description)
          if resp:
              print('[CARD MGMT] authorized and posted ', amount, ' to card ', cardNumber)
          else:
              print('[CARD MGMT] unable to post ', amount, ' to card ', cardNumber)
              ack =  False

      else:
          print('[CARD MGMT] unable to authorize ', amount, ' to card ', cardNumber)
      return ack

    def getTransactions(self, cardNumber, numOfResults, dateRange, amountRange, entryMode):
      resp = self.TransactionHistoryClient.filterTransactions(cardNumber, numOfResults, dateRange, amountRange, entryMode, '')
      return resp

    def searchTransactions(self, cardNumber, description):
      resp = self.TransactionHistoryClient.filterTransactions(cardNumber, 0, '', '', '', description)
      return resp

    def changeAuthorizationRule(self, cardNumber, amount):
      ack = self.PaymentAuthorizationClient.changeAuthRule(cardNumber, amount)
      return ack


if __name__ == '__main__':
    # setting up the interface for this service
    handler = CardManagementHandler()
    processor = CardManagement.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the CardManagementServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] CardManagementServer done.')
