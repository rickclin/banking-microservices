#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import AccountInformation, AccountInformationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('0.0.0.0', 9090)

class AccountInformationHandler:
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

    def getBalance(self, accountNumber):
      clientAcctInfoDB, transportAcctInfoDB = self.createConnection('account-information-db', AccountInformationDB)
      balance = clientAcctInfoDB.getBalance(accountNumber)
      transportAcctInfoDB.close()
      return balance

    def updateBalance(self, accountNumber, amount):
      clientAcctInfoDB, transportAcctInfoDB = self.createConnection('account-information-db', AccountInformationDB)
      newBalance = clientAcctInfoDB.updateBalance(accountNumber, amount)
      transportAcctInfoDB.close()
      return newBalance

if __name__ == '__main__':
    handler = AccountInformationHandler()
    processor = AccountInformation.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the AccountInformationServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' AccountInformationServer done.')
