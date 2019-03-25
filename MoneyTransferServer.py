#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import MoneyTransfer, AccountInformation

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19105)

class MoneyTransferHandler:
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

    def transferMoney(self, fromAccount, toAccount, amount):
      clientAcctInfo, transportAcctInfo = self.createConnection(19104, AccountInformation)
      bal_fromAccount = clientAcctInfo.getBalance(fromAccount)
      bal_toAccount   = clientAcctInfo.getBalance(toAccount)
      amount = float(amount)
      if bal_fromAccount == 'n/a' or bal_toAccount == 'n/a':
        print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] The specified account(s) does not exist!')
        transportAcctInfo.close()
        return False
      else:
        if amount > float(bal_fromAccount):
          print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Insufficient funds!')
          transportAcctInfo.close()
          return False
        else:
          bal_fromAccount = float(bal_fromAccount)
          bal_toAccount   = float(bal_toAccount)
          assert float(clientAcctInfo.updateBalance(fromAccount, str(-1*amount))) == bal_fromAccount - amount
          assert float(clientAcctInfo.updateBalance(toAccount,   str(amount)))    == bal_toAccount   + amount
          transportAcctInfo.close()
          return True

if __name__ == '__main__':
    handler = MoneyTransferHandler()
    processor = MoneyTransfer.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the MoneyTransferServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' MoneyTransferServer done.')
