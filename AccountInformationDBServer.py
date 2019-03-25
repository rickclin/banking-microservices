#!/usr/bin/env python

import glob
import sys
import datetime

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import AccountInformationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19106)
ACCOUNT_BALANCE = {'accountNumber': 'balance', '0000000000000000': 50.00}

class AccountInformationDBHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def getBalance(self, accountNumber):
      balance = ACCOUNT_BALANCE[accountNumber] if accountNumber in ACCOUNT_BALANCE.keys() \
                                               else 'n/a'
      return str(balance)

    def updateBalance(self, accountNumber, amount):
      global ACCOUNT_BALABCE
      if accountNumber not in ACCOUNT_BALANCE.keys():
        return 'n/a'
      else:
        balance = ACCOUNT_BALANCE[accountNumber]
        balance = balance + float(amount)
        ACCOUNT_BALANCE[accountNumber] = balance
        return str(balance)

    def addAccount(self, accountNumber):
      global ACCOUNT_BALANCE
      if accountNumber in ACCOUNT_BALANCE.keys():
        return False
      else:
        ACCOUNT_BALANCE[accountNumber] = float(0.00);
        return True

if __name__ == '__main__':
    handler = AccountInformationDBHandler()
    processor = AccountInformationDB.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the AccountInformationDBServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' AccountInformationDBServer done.')
