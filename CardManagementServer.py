#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import CardManagement, TransactionHistory, PaymentAuthorization

from datetime         import datetime

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

card_db = ['1234123412341234']
auth_rule_db = {'1234123412341234' : 300}
tranx_db = {'1234123412341234' : []}

class CardManagementHandler:
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

    def authorizePayment(self, cardNumber, amount):
      auth = False
      limit = auth_rule_db[cardNumber]
      resp = str(amount) + ' exceeds the transaction limit ' + str(limit)

      if amount <= limit:
        timestamp = str(datetime.now())
        tranx_db[cardNumber].append(str(amount) + ', ' + timestamp)
        auth = True
        resp = str(amount) + ' posted to ' + cardNumber[-4:] + \
               ' at ' + timestamp

      return resp

    def getTransactionHistory(self, cardNumber):
      history = tranx_db[cardNumber]
      return history
      #for entry in history:
      #  print(entry)
    
    def getCardNumbers(self):
      return card_db[0]

    def postTransaction(self, cardNumber, description, amount, entryMode):
      # 1. authorize payment
      clientPaymentAuth, transportPaymentAuth = self.createConnection(19096, PaymentAuthorization)
      ack = clientPaymentAuth.authorize(amount, cardNumber)
      transportPaymentAuth.close()
      if ack:
          # 2. insert transaction
          clientTranxHist, transportTranxHist = self.createConnection(19095, TransactionHistory)
          resp = clientTranxHist.insertTransaction(cardNumber, amount, entryMode, description)
          transportTranxHist.close()         
          if resp:
              print('authorized and posted ', amount, ' to card ', cardNumber)
          else:
              print('unable to post ', amount, ' to card ', cardNumber)
              ack =  False

      else:
          print('unable to authorize ', amount, ' to card ', cardNumber)

      return ack

    def getTransactions(self, cardNumber, numOfResults, dateRange, entryMode):
      return ["", ""]

    def searchTransactions(self, cardNumber, description):
      return ["", ""]

    def changeAuthorizationRule(self, cardNumber, amount):
      return True

if __name__ == '__main__':
    # setting up the interface for this service
    handler = CardManagementHandler()
    processor = CardManagement.Processor(handler)
    transport = TSocket.TServerSocket(host='localhost', port=19093)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    
    print('Starting the server...')
    server.serve()
    print('Card Management done.')