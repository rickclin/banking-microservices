#!/usr/bin/python
import sys
sys.path.append('gen-py')

from bank import HelloworldService, AuthenticateService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import time

def main():
  # Make socket
  transport = TSocket.TSocket('localhost', 19090)
  transportAuth = TSocket.TSocket('localhost', 19092)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
  transportAuth = TTransport.TBufferedTransport(transportAuth)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  protocolAuth = TBinaryProtocol.TBinaryProtocol(transportAuth)

  # Create a client to use the protocol encoder
  client = HelloworldService.Client(protocol)
  clientAuth = AuthenticateService.Client(protocolAuth)

  # Connect!
  transport.open()
  transportAuth.open()
  print("conn open")
  print("conn Auth open")
  res = client.getHelloworld()
  print(res)
  username = raw_input('username: ')
  password = raw_input('password: ')

  auth = clientAuth.authenticate(username, password)

  if auth:
    print("successfully authenticated!")
  else:
    print("authentication failed!")

  transport.close()
  transportAuth.close()

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
