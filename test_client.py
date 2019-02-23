#!/usr/bin/python
import sys
sys.path.append('gen-py')

from bank             import HelloworldService      # 19090
from bank             import CardManagement         # 19093
from bank             import CustomerInformation    # 19094
from bank             import PaymentAuthorization   # 19096
from bank             import PaymentAuthorizationDB # 19098
from bank             import TransactionHistory     # 19095 
from bank             import TransactionHistoryDB   # 19097

from thrift           import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol

import time
import getpass
import random
import string

def createConnection(port, service):
    transport = TSocket.TSocket('localhost', port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = service.Client(protocol)
    transport.open()
    return client, transport


def main():
  # Make socket
  client,         transport         = createConnection(19090, HelloworldService) 
  # clientCard,     transportCard     = createConnection(19093) 
  # clientCustomer, transportCustomer = createConnection(19094) 
  clientAuth,     transportAuth     = createConnection(19096, PaymentAuthorization) 
  clientAuthDB,   transportAuthDB   = createConnection(19098, PaymentAuthorizationDB) 
  clientTranx,    transportTranx    = createConnection(19095, TransactionHistory) 
  clientTranxDB,  transportTranxDB  = createConnection(19097, TransactionHistoryDB) 

  print("connections opened!")
  
  # verify servers are up
  res = client.getHelloworld()
  print(res)
  transport.close() 
  
  # communicating with Payment Authorization DB server
  print('[TEST] Payment Authorization DB Server')
  print(clientAuthDB.getLimit   ('0000000000000000'))
  print(clientAuthDB.changeLimit('0000000000000000', 99.99))
  print(clientAuthDB.getLimit   ('0000000000000000'))
  print(clientAuthDB.addLimit   ('0000000000001234', 50.00))
  print(clientAuthDB.getLimit   ('0000000000001234'))
  print(clientAuthDB.changeLimit('0000000000000000', 500.00))
  print(clientAuthDB.getLimit   ('0000000000000000'))
  transportAuthDB.close()
  input('[PAUSE] Press Return to continue...')

  # communicating with Payment Authorization
  print('[TEST] Payment Authorization Server')
  assert clientAuth.authorize     ('0000000000000000', 0.00  ) == True
  assert clientAuth.authorize     ('0000000000000000', 499.99) == True
  assert clientAuth.authorize     ('0000000000000000', 500.01) == False
  assert clientAuth.authorize     ('9999000000001234', 500.01) == False
  assert clientAuth.changeAuthRule('0000000000000000', 999.99) == True
  assert clientAuth.changeAuthRule('9999000000001234', 999.99) == False
  assert clientAuth.authorize     ('0000000000000000', 0.00  ) == True
  assert clientAuth.authorize     ('0000000000000000', 499.99) == True
  assert clientAuth.authorize     ('0000000000000000', 500.01) == True
  assert clientAuth.authorize     ('9999000000001234', 500.01) == False
  transportAuth.close()
  input('[PAUSE] Press Return to continue...')

  # communicating with Transaction History DB server
  print('[TEST] Transaction History DB Server')
  initial_log = clientTranxDB.getTransactionLog('0000000000000000')
  print('[TEST] ' + str(len(initial_log)) + ' entries already exist!')
  print('[TEST] Inserting more transactions...')
  for i in range(0,200):
    digit = random.randint(1, 100)
    dec   = random.randint(1, 100) / 100
    amount= digit + dec
    entry = ['chip', 'swipe', 'online'][digit%3]
    des = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    clientTranxDB.insertTransaction('0000000000000000', amount, entry, des)
    time.sleep(dec*0.05)
  print('[TEST] Displays the complete transaction log')
  update_log = clientTranxDB.getTransactionLog('0000000000000000')
  print('\n'.join(update_log))
  transportTranxDB.close()
  print('[TEST] ' + str(len(update_log)) + ' entries are now in the card history!')
  input('[PAUSE] Press Return to continue...')

  # communicating with Transaction History server
  print('[TEST] Transaction History Server')
  print('[TEST] Transactions by card ending in 0000: all')
  print('\n'.join(clientTranx.getTransactionLog('0000000000000000')))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: all between $10-$20')
  match = clientTranx.filterTransactions('0000000000000000', 0, '', '10, 20', '', '')
  print('[TEST] ' + str(len(match)) + ' matching transactions')
  print('\n'.join(match))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: all under swipe entry mode')
  match = clientTranx.filterTransactions('0000000000000000', 0, '', '', 'swipe', '')
  print('[TEST] ' + str(len(match)) + ' matching transactions')
  print('\n'.join(match))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: all between 02-22 and 02-24')
  match = clientTranx.filterTransactions('0000000000000000', 0, '2019-02-22, 2019-02-25', '', '', '')
  print('[TEST] ' + str(len(match)) + ' matching transactions: ')
  print('\n'.join(match))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: all containing \'Z\' in their descriptions')
  match = clientTranx.filterTransactions('0000000000000000', 0, '', '', '', 'Z')
  print('[TEST] ' + str(len(match)) + ' matching transactions: ')
  print('\n'.join(match))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: all between $10-$20, swipe entered, from 2/22-2/25')
  match = clientTranx.filterTransactions('0000000000000000', 0, '2019-02-22, 2019-02-26', '10, 20', 'swipe', '')
  print('[TEST] ' + str(len(match)) + ' matching transactions: ')
  print('\n'.join(match))
  input('[PAUSE] Press Return to continue')
  print('[TEST] Transactions by card ending in 0000: first 5 between $10-$20, swipe entered, from 2/22-2/25')
  match = clientTranx.filterTransactions('0000000000000000', 5, '2019-02-22, 2019-02-26', '10, 20', 'swipe', '')
  print('[TEST] ' + str(len(match)) + ' matching transactions: ')
  print('\n'.join(match))
  transportTranx.close()
  input('[PAUSE] Press Return to continue')
  
  # transportCard.close()
  # transportCustomer.close()
  # transportAuthDB.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
