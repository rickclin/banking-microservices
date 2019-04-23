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

import thriftpy2
from thriftpy2.rpc              import make_client
from thriftpy2.protocol.binary  import TBinaryProtocolFactory
from thriftpy2.transport.framed import TFramedTransportFactory
import thrift_connector.connection_pool as connection_pool
bank_thrift = thriftpy2.load("bank.thrift", module_name="bank_thrift")

SERVER_PORT = ('0.0.0.0', 9090)

class MoneyTransferHandler:
    def __init__(self):
        self.log = {}
        self.AccountInformationClient = connection_pool.ClientPool(
          bank_thrift.AccountInformation,
          'account-information', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )

    def ping(self):
        print('ping()')

    def transferMoney(self, fromAccount, toAccount, amount):
      bal_fromAccount = self.AccountInformationClient.getBalance(fromAccount)
      bal_toAccount   = self.AccountInformationClient.getBalance(toAccount)
      amount = float(amount)
      if bal_fromAccount == 'n/a' or bal_toAccount == 'n/a':
        print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] The specified account(s) does not exist!')
        return False
      else:
        if amount > float(bal_fromAccount):
          print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Insufficient funds!')
          return False
        else:
          bal_fromAccount = float(bal_fromAccount)
          bal_toAccount   = float(bal_toAccount)
          assert float(self.AccountInformationClient.updateBalance(fromAccount, str(-1*amount))) == bal_fromAccount - amount
          assert float(self.AccountInformationClient.updateBalance(toAccount,   str(amount)))    == bal_toAccount   + amount
          return True

if __name__ == '__main__':
    handler = MoneyTransferHandler()
    processor = MoneyTransfer.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the MoneyTransferServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' MoneyTransferServer done.')
