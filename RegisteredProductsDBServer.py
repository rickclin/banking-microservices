#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import RegisteredProductsDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19102)
CUSTOMER_CARDS = {'customerId':['number'], 'ricklin' : ['4414098724561099', '4414098707079243']}
CUSTOMER_ACCOUNTS = {'customerId':['number'], 'ricklin' : ['5563219190', '3721108094']}

class RegisteredProductsDBHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def getAccountNumbers(self, customerId):
      accounts = CUSTOMER_ACCOUNTS[customerId]
      return accounts

    def getCardNumbers(self, customerId):
      cards = CUSTOMER_CARDS[customerId]
      return cards

    def addCard(self, customerId):
      global CUSTOMER_CARDS

      newCardNumber = ''.join(random.choice(string.digits) for _ in range(16))
      while any(newCardNumber in entry for entry in CUSTOMER_CARDS.values()):
        newCardNumber = ''.join(random.choice(string.digits) for _ in range(16))
      
      if customerId not in CUSTOMER_CARDS.keys():
        CUSTOMER_CARDS[customerId] = []

      CUSTOMER_CARDS[customerId].append(newCardNumber)
      print('['+SERVER_PORT[0]+':'+str(SERVER_PORT[1])+'] card created: ' + newCardNumber + ' for ' + customerId)

      return newCardNumber

    def addAccount(self, customerId):
      global CUSTOMER_ACCOUNTS

      newAccountNumber = ''.join(random.choice(string.digits) for _ in range(10))
      while any(newAccountNumber in entry for entry in CUSTOMER_ACCOUNTS.values()):
        newAccountNumber = ''.join(random.choice(string.digits) for _ in range(10))
 
      if customerId not in CUSTOMER_ACCOUNTS.keys():
        CUSTOMER_ACCOUNTS[customerId] = []

      CUSTOMER_ACCOUNTS[customerId].append(newAccountNumber)
      print('['+SERVER_PORT[0]+':'+str(SERVER_PORT[1])+'] account created: ' + newAccountNumber + ' for ' + customerId)
      return newAccountNumber

if __name__ == '__main__':
    handler = RegisteredProductsDBHandler()
    processor = RegisteredProductsDB.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the RegisteredProductsDBServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' RegisteredProductsDBServer done.')
