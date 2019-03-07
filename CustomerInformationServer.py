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

SERVER_PORT = ('localhost', 19094)

class CustomerInformationHandler:
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

    def retrieveContactInformation(self, customerId):
      clientContact, transportContact = self.createConnection(19099, ContactInformation)
      contact = clientContact.retrieveCustomer(customerId)
      transportContact.close()
      return contact

    def updateContactInformation(self, customerId, revisedInfo):
      clientContact, transportContact = self.createConnection(19099, ContactInformation)
      ack = clientContact.updateContactInformation(customerId, revisedInfo)
      transportContact.close()
      return ack

    def verifyContactInformation(self, customerId, field, answer):
      clientContact, transportContact = self.createConnection(19099, ContactInformation)
      contact =  clientContact.retrieveCustomer(customerId)
      transportContact.close()
      if contact[field] == answer:
        return True
      else:
        return False

    def getRegisteredProducts(self, customerId):
      clientProducts, transportProducts = self.createConnection(19100, RegisteredProducts)
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
      clientProducts, transportProducts = self.createConnection(19100, RegisteredProducts)
      newAccountNumber = clientProducts.addAccount(customerId)
      transportProducts.close()
      return newAccountNumber
   
    def newCard(self, customerId):
      clientProducts, transportProducts = self.createConnection(19100, RegisteredProducts)
      newCardNumber = clientProducts.addCard(customerId)
      transportProducts.close()
      return newCardNumber

if __name__ == '__main__':
    handler = CustomerInformationHandler()
    processor = CustomerInformation.Processor(handler)
    transport = TSocket.TServerSocket(host='localhost', port=19094)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the CustomerInformationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] CustomerInformationServer done.')
