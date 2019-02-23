#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import CustomerInformation

from datetime         import datetime

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

contact_info_db = { 'ricklin' : { 'number' : '6666666666', 'address' : '123 Broadway N'}}
customer_product_db = { 'ricklin' : ['checking', 'savings', 'platinum card']}

class CustomerInformationHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def getContactInformation(self, customerId):
      info = contact_info_db[customerId]
      return info

    def getRegisteredProducts(self, customerId):
      products = customer_product_db[customerId]
      return products
  
    def retrieveContactInformation(self, customerId):
      info = clientContactInformation.searchCustomer(customemrId)
      return info

    def updateContactInformation(self, customerId, revisedInfo):
      return clientContactInformation.updateContactInformation(customerId, revisedInfo)

    def verifyContactInformation(self, customerId, field, answer):
      info = clientContactInformation.searchCustomer(customerId)
      info = info.split(',')
      if info[field] == answer: # there should be an enum from field to info indexes
        return True
      else:
        return False

    def getRegisteredProducts(self, customerId):
      products = clientRegisteredProducts.getRegisteredProducts(customerId)
      return products

    def getAccountNumbers(self, customerId):
      products = clientRegisteredProducts.getRegisteredProducts(customerId)
      accounts = products # extract account numbers from query
      return accounts

    def getCardNumbers(self, customerId):
      products = clientRegisteredProducts.getRegisteredProducts(customerId)
      cards = products # extract card numbers from query
      return cards

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

    print('Starting the server...')
    server.serve()
    print('Customer Information done.')
