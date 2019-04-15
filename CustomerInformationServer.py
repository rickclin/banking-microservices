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

SERVER_PORT = ('0.0.0.0', 9090)

class CustomerInformationHandler:
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

    def retrieveContactInformation(self, customerId):
      clientContact, transportContact = self.createConnection('contact-information', ContactInformation)
      contact = clientContact.retrieveCustomer(customerId)
      transportContact.close()
      return contact

    def updateContactInformation(self, customerId, revisedInfo):
      clientContact, transportContact = self.createConnection('contact-information', ContactInformation)
      ack = clientContact.updateContactInformation(customerId, revisedInfo)
      transportContact.close()
      return ack

    def verifyContactInformation(self, customerId, field, answer):
      clientContact, transportContact = self.createConnection('contact-information', ContactInformation)
      contact =  clientContact.retrieveCustomer(customerId)
      transportContact.close()
      if contact[field] == answer:
        return True
      else:
        return False

    def getRegisteredProducts(self, customerId):
      clientProducts, transportProducts = self.createConnection('registered-products', RegisteredProducts)
      products = clientProducts.getRegisteredProducts(customerId)
      transportProducts.close()
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
      clientProducts, transportProducts = self.createConnection('registered-products', RegisteredProducts)
      newAccountNumber = clientProducts.addAccount(customerId)
      transportProducts.close()
      return newAccountNumber
   
    def newCard(self, customerId):
      clientProducts, transportProducts = self.createConnection('registered-products', RegisteredProducts)
      newCardNumber = clientProducts.addCard(customerId)
      transportProducts.close()
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
