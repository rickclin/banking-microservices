#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import ContactInformation, ContactInformationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19099)

class ContactInformationHandler:
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

    def retrieveCustomer(self, customerId):
      clientContactDB, transportContactDB = self.createConnection(19101, ContactInformationDB)
      contact = clientContactDB.retrieveCustomer(customerId)
      return contact

    def updateContactInformation(self, customerId, revisedInfo):
      clientContactDB, transportContactDB = self.createConnection(19101, ContactInformationDB)
      ack = clientContactDB.updateContactInformation(customerId, revisedInfo)
      return ack


if __name__ == '__main__':
    handler = ContactInformationHandler()
    processor = ContactInformation.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the ContactInformationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' ContactInformationServer done.')
