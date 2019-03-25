#!/usr/bin/env python

import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import OnlineBanking, AccountInformation, MoneyTransfer

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('localhost', 19103)

class OnlineBankingHandler:
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

    def getBalance(self, accountNumber):
      clientAcctInfo, transportAcctInfo = self.createConnection(19104, AccountInformation)
      balance = clientAcctInfo.getBalance(accountNumber)
      transportAcctInfo.close()
      return balance

    def transferMoney(self, fromAccount, toAccount, amount):
      clientMoneyTx, transportMoneyTx = self.createConnection(19105, MoneyTransfer)
      ack = clientMoneyTx.transferMoney(fromAccount, toAccount, amount)
      transportMoneyTx.close()
      return ack


if __name__ == '__main__':
    handler = OnlineBankingHandler()
    processor = OnlineBanking.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the OnlineBankingServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] OnlineBankingServer done.')
