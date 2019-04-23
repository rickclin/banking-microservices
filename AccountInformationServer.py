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

import thriftpy2
from thriftpy2.rpc              import make_client
from thriftpy2.protocol.binary  import TBinaryProtocolFactory
from thriftpy2.transport.framed import TFramedTransportFactory
import thrift_connector.connection_pool as connection_pool
bank_thrift = thriftpy2.load("bank.thrift", module_name="bank_thrift")

SERVER_PORT = ('0.0.0.0', 9090)

class AccountInformationHandler:
    def __init__(self):
        self.log = {}
        self.AccountInformationDBClient = connection_pool.ClientPool(
          bank_thrift.AccountInformationDB,
          'account-information-db', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )

    def ping(self):
        print('ping()')

    def getBalance(self, accountNumber):
      balance = self.AccountInformationDBClient.getBalance(accountNumber)
      return balance

    def updateBalance(self, accountNumber, amount):
      newBalance = self.AccountInformationDBClient.updateBalance(accountNumber, amount)
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
