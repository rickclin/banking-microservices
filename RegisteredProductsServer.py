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

SERVER_PORT = ('0.0.0.0', 9090)

class RegisteredProductsHandler:
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

    def getRegisteredProducts(self, customerId):
      clientProdDB, transportProdDB = self.createConnection('registered-products-db', RegisteredProductsDB)
      products = {}
      cards = clientProdDB.getCardNumbers(customerId)
      accounts = clientProdDB.getAccountNumbers(customerId)
      transportProdDB.close()
      products["cards"] = cards
      products["accounts"] = accounts
      return products

    def addCard(self, customerId):
      clientProdDB, transportProdDB = self.createConnection('registered-products-db', RegisteredProductsDB)
      newCardNumber = clientProdDB.addCard(customerId)
      transportProdDB.close()
      return newCardNumber

    def addAccount(self, customerId):
      clientProdDB, transportProdDB = self.createConnection('registered-products-db', RegisteredProductsDB)
      newAccountNumber = clientProdDB.addAccount(customerId)
      transportProdDB.close()
      return newAccountNumber

if __name__ == '__main__':
    handler = RegisteredProductsHandler()
    processor = RegisteredProducts.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the RegisteredProductsServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' RegisteredProductsServer done.')
