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

import thriftpy2
from thriftpy2.rpc              import make_client
from thriftpy2.protocol.binary  import TBinaryProtocolFactory
from thriftpy2.transport.framed import TFramedTransportFactory
import thrift_connector.connection_pool as connection_pool
bank_thrift = thriftpy2.load("bank.thrift", module_name="bank_thrift")

SERVER_PORT = ('0.0.0.0', 9090)

class RegisteredProductsHandler:
    def __init__(self):
        self.log = {}
        self.RegisteredProductsDBClient = connection_pool.ClientPool(
          bank_thrift.RegisteredProductsDB,
          'registered-products-db', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )

    def ping(self):
        print('ping()')
    
    def getRegisteredProducts(self, customerId):
      products = {}
      cards = self.RegisteredProductsDBClient.getCardNumbers(customerId)
      accounts = self.RegisteredProductsDBClient.getAccountNumbers(customerId)
      products["cards"] = cards
      products["accounts"] = accounts
      return products

    def addCard(self, customerId):
      newCardNumber = self.RegisteredProductsDBClient.addCard(customerId)
      return newCardNumber

    def addAccount(self, customerId):
      newAccountNumber = self.RegisteredProductsDBClient.addAccount(customerId)
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
