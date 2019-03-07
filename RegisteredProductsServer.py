#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import RegisteredProducts, RegisteredProductsDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19100)

class RegisteredProductsHandler:
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

    def getRegisteredProducts(self, customerId):
      clientProdDB, transportProdDB = self.createConnection(19102, RegisteredProductsDB)
      products = {}
      cards = clientProdDB.getCardNumbers(customerId)
      accounts = clientProdDB.getAccountNumbers(customerId)
      transportProdDB.close()
      products["cards"] = cards
      products["accounts"] = accounts
      return products

    def addCard(self, customerId):
      clientProdDB, transportProdDB = self.createConnection(19102, RegisteredProductsDB)
      newCardNumber = clientProdDB.addCard(customerId)
      transportProdDB.close()
      return newCardNumber

    def addAccount(self, customerId):
      clientProdDB, transportProdDB = self.createConnection(19102, RegisteredProductsDB)
      newAccountNumber = clientProdDB.addAccount(customerId)
      transportProdDB.close()
      return newAccountNumber

if __name__ == '__main__':
    handler = RegisteredProductsHandler()
    processor = RegisteredProducts.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the RegisteredProductsDBServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' RegisteredProductsDBServer done.')
