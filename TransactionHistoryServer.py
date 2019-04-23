#!/usr/bin/env python
import glob
import sys
sys.path.append('gen-py')

from thrift           import Thrift
from bank             import TransactionHistory 
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

import datetime
import string

SERVER_PORT = ('0.0.0.0', 9090)

class TransactionHistoryHandler:
    def __init__(self):
        self.log = {}
        self.TransactionHistoryDBClient = connection_pool.ClientPool(
          bank_thrift.TransactionHistoryDB,
          'transaction-history-db', 9090,
          connection_class=connection_pool.ThriftPyCyClient
        )
 
    def ping(self):
        print('ping()')
    
    def getTransactionLog(self, cardNumber):
      log = self.TransactionHistoryDBClient.getTransactionLog(cardNumber)
      return log

    def filterTransactions(self, cardNumber, numOfResults, dateRange, amountRange, entryMode, description):
      log = self.TransactionHistoryDBClient.getTransactionLog(cardNumber)
      output = []
      
      dateRange = dateRange.split(',')
      amountRange = amountRange.split(',')
      startDate = datetime.datetime.strptime(dateRange[0].strip(), '%Y-%m-%d') if len(dateRange) > 1 else ''
      endDate   = datetime.datetime.strptime(dateRange[1].strip(), '%Y-%m-%d') if len(dateRange) > 1 else ''
      startAmount = float(amountRange[0]) if len(amountRange) > 1 else 0
      endAmount   = float(amountRange[1]) if len(amountRange) > 1 else 0
      
      for entryRaw in log:
        entry = entryRaw.split(',')
        date = datetime.datetime.strptime(entry[0], '%Y-%m-%dT%H:%M:%S.%f')
        amount = float(entry[2])
        if entry[1] != cardNumber: continue
        if len(dateRange) > 1:
          if date <= startDate or date >= endDate: continue
        if len(amountRange) > 1:
          if amount < startAmount or amount > endAmount: continue
        if entryMode != '':
          if entry[3] != entryMode: continue
        if description != '':
          if description not in entry[4]: continue
        output.append(entryRaw)
      
      return output[:int(numOfResults)] if numOfResults > 0 else output

    def insertTransaction(self, cardNumber, amount, entryMode, description):
      ack = self.TransactionHistoryDBClient.insertTransaction(cardNumber, amount, entryMode, description)
      return ack


if __name__ == '__main__':
    handler = TransactionHistoryHandler()
    processor = TransactionHistory.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] Starting the TransactionHistoryServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + '] TransactionHistoryServer done.')
