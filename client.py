#!/usr/bin/python
import sys
sys.path.append('gen-py')

from bank import HelloworldService, AuthenticateService, CardManagement, CustomerInformation

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import time
import getpass

def main():
  # Make socket
  transport = TSocket.TSocket('localhost', 19090)
  transportAuth = TSocket.TSocket('localhost', 19092)
  transportCard = TSocket.TSocket('localhost', 19093)
  transportCustomer = TSocket.TSocket('localhost', 19094)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
  transportAuth = TTransport.TBufferedTransport(transportAuth)
  transportCard = TTransport.TBufferedTransport(transportCard)
  transportCustomer = TTransport.TBufferedTransport(transportCustomer)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  protocolAuth = TBinaryProtocol.TBinaryProtocol(transportAuth)
  protocolCard = TBinaryProtocol.TBinaryProtocol(transportCard)
  protocolCustomer = TBinaryProtocol.TBinaryProtocol(transportCustomer)

  # Create a client to use the protocol encoder
  client = HelloworldService.Client(protocol)
  clientAuth = AuthenticateService.Client(protocolAuth)
  clientCard = CardManagement.Client(protocolCard)
  clientCustomer = CustomerInformation.Client(protocolCustomer)

  # Connect!
  transport.open()
  transportAuth.open()
  transportCard.open()
  transportCustomer.open()
  print("connections opened!")
  
  # verify servers are up
  res = client.getHelloworld()
  print(res)

  # username: ricklin; password: password
  username = raw_input('username: ')
  password = getpass.getpass('password: ')
  auth = clientAuth.authenticate(username, password)
  login = False

  if auth:
    print("successfully authenticated!")
    login = True
    print("logged in as " + username)
  else:
    print("authentication failed!")

  while login:
    card = clientCard.getCardNumber()
    opt = raw_input("1: authorize payment; 2: get history; 3: get contact; 4: get products; 5: log out ----  ")
    if int(opt) == 1:
      amount = float(raw_input("enter payment amount: "))
      print(clientCard.authorizePayment(card, amount))
    elif int(opt) == 2:
      history = clientCard.getTransactionHistory(card)
      for entry in history:
        print(entry)
    elif int(opt) == 3:
      info = clientCustomer.getContactInformation(username)
      print username + " can be reached at " + info['number'] + " or " + info['address']
    elif int(opt) == 4:
      products = clientCustomer.getRegisteredProducts(username)
      print "the following products are activated by " + username
      for product in products:
        print(product)
    elif int(opt) == 5:
      login = False

  transport.close()
  transportAuth.close()
  transportCard.close()
  transportCustomer.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
