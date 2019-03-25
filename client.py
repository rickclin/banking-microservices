#!/usr/bin/python3
import sys
sys.path.append('gen-py')

# Importe defined microservice handlers
from bank import AuthenticateService  # 19092
AUTH_SERVER_PORT = ('localhost', 19092)
from bank import CardManagement       # 19093
CARD_SERVER_PORT = ('localhost', 19093)
from bank import CustomerInformation  # 19094
CUST_SERVER_PORT = ('localhost', 19094)
from bank import OnlineBanking        # 19103
OLBK_SERVER_PORT = ('localhost', 19103)

from thrift           import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol

import time
import getpass
import os

def createConnection(port, server):
  transport = TSocket.TSocket('localhost', port)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = server.Client(protocol)
  transport.open()
  return client, transport

def print_intro():
  print("   ___        _ _              ____              _    _             ") 
  print("  / _ \ _ __ | (_)_ __   ___  | __ )  __ _ _ __ | | _(_)_ __   __ _ ") 
  print(" | | | | '_ \| | | '_ \ / _ \ |  _ \ / _` | '_ \| |/ / | '_ \ / _` |")
  print(" | |_| | | | | | | | | |  __/ | |_) | (_| | | | |   <| | | | | (_| |")
  print("  \___/|_| |_|_|_|_| |_|\___| |____/ \__,_|_| |_|_|\_\_|_| |_|\__, |")
  print("                                               By Cornell SAIL|___/ ")
  print("")
  print("")

def main():
  
  #clientOnlineBanking,      transportOnlineBanking      = createConnection(OLBK_SERVER_PORT[0], OLBK_SERVER_PORT[1], OnlineBanking)

  #print("connections opened!")
 
  session_active      = False
  session_customerId  = ''

  while True:
    while not session_active:
      os.system('clear')
      print_intro()
      # username: ricklin; password: password
      username = input(          'username: ')
      password = getpass.getpass('password: ')
      clientUserAuthentication, transportUserAuthentication = \
        createConnection(AUTH_SERVER_PORT[1], AuthenticateService)
      session_active = clientUserAuthentication.authenticate(username, password)
      transportUserAuthentication.close()

      if session_active:
        session_customerId = username
        input("Logged in as " + username)
      else:
        input("Incorrect username or password. Please try again!")
      
    while session_active:
      os.system('clear')
      opt = input("1: Credit Cards; 2: Personal Information; 3: Accounts 4: Log out ---> ")
      if   int(opt) == 1: pass
        clientCustomerInformation,transportCustomerInformation= \
          createConnection(CUST_SERVER_PORT[0], CUST_SERVER_PORT[1], CustomerInformation)
        cards = clientCustomerInformation.getRegisteredProducts(session_customerId).['cards']


      clientCardManagement,     transportCardManagement     = \
        createConnection(CARD_SERVER_PORT[0], CARD_SERVER_PORT[1], CardManagement)
      
      elif int(opt) == 2: pass
        
      elif int(opt) == 3: pass
        
      elif int(opt) == 4:
        session_active = False
        session_customerId = ''

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
