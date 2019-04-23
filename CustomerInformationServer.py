#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import CustomerInformation, RegisteredProducts, ContactInformation

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

class CustomerInformationHandler:
    def __init__(self):
        self.log = {}
        self.ContactInformationClient = connection_pool.ClientPool(
          bank_thrift.ContactInformation,
          'contact-information', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )
        self.RegisteredProductsClient = connection_pool.ClientPool(
          bank_thrift.RegisteredProducts,
          'registered-products', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )

    def ping(self):
        print('ping()')

    def retrieveContactInformation(self, customerId):
      contact = self.ContactInformationClient.retrieveCustomer(customerId)
      return contact

    def updateContactInformation(self, customerId, revisedInfo):
      ack = self.ContactInformationClient.updateContactInformation(customerId, revisedInfo)
      return ack

    def verifyContactInformation(self, customerId, field, answer):
      contact =  self.ContactInformationClient.retrieveCustomer(customerId)
      if contact[field] == answer:
        return True
      else:
        return False

    def getRegisteredProducts(self, customerId):
      products = self.RegisteredProductsClient.getRegisteredProducts(customerId)
      return products

    def getAccountNumbers(self, customerId):
      products = self.getRegisteredProducts(customerId)
      accounts = products['accounts']
      return accounts

    def getCardNumbers(self, customerId):
      products = self.getRegisteredProducts(customerId)
      cards = products['cards']
      return cards

    def newAccount(self, customerId):
      newAccountNumber = self.RegisteredProductsClient.addAccount(customerId)
      return newAccountNumber
   
    def newCard(self, customerId):
      newCardNumber = self.RegisteredProductsClient.addCard(customerId)
      return newCardNumber

if __name__ == '__main__':
    handler = CustomerInformationHandler()
    processor = CustomerInformation.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the CustomerInformationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] CustomerInformationServer done.')
