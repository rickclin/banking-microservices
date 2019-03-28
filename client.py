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
import atexit

def exit_cleanup():
  os.system('clear')

atexit.register(exit_cleanup)

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
      print("Welcome back " + username + "!")
      print("An overview of your accounts")
      clientCustomerInformation,transportCustomerInformation= \
        createConnection(CUST_SERVER_PORT[1], CustomerInformation)
      products = clientCustomerInformation.getRegisteredProducts(session_customerId)
      transportCustomerInformation.close()
      
      clientOnlineBanking,      transportOnlineBanking      = \
        createConnection(OLBK_SERVER_PORT[1], OnlineBanking)
      
      print("--------------------------------------------- Update Personal Information (1)")
      
      for account in products["accounts"]:
        print("Account {:>16} $ {:>20,.02f}".format(account, float(clientOnlineBanking.getBalance(account))))

      print("------------------------------------------------------------ More Actions (2)")
      
      for card in products["cards"]:
        print("Card    {:>16} $ {:>20,.02f}".format(card, float(clientOnlineBanking.getBalance(card))))
     
      transportOnlineBanking.close()
      print("------------------------------------------------------------ More Actions (3)")
      print("----------------------------------------------------------------- Log Out (X)")
      print("")
      opt = input("Action ------------------------------------------------------------------> ")

      if opt == '1':
        pass
      elif opt == '2':
        os.system('clear')
        clientOnlineBanking,      transportOnlineBanking      = \
          createConnection(OLBK_SERVER_PORT[1], OnlineBanking)

        print("Select an account -----------------------------------------------------------")
        i = 1
        for account in products["accounts"]:
          print("({}) {:>16} $ {:>20,.02f}".format(i, account, float(clientOnlineBanking.getBalance(account))))
          i+= 1

        print("-----------------------------------------------------------------------------")
        print("")
        transportOnlineBanking.close()
        account_sel = input("Action ------------------------------------------------------------------> ")
        os.system('clear')
        clientOnlineBanking,      transportOnlineBanking      = \
          createConnection(OLBK_SERVER_PORT[1], OnlineBanking)       
        print("-----------------------------------------------------------------------------")
        print("({}) {:>16} $ {:>20,.02f}".format(i, products["accounts"][int(account_sel)], float(clientOnlineBanking.getBalance(products["accounts"][int(account_sel)-1]))))
        print("----------------------------------------------------------- Make Transfer (1)")
        print("")
        transportOnlineBanking.close()
        transfer = input("Action ------------------------------------------------------------------> ")
        if transfer == '1':
          os.system('clear')
          clientOnlineBanking,      transportOnlineBanking      = \
            createConnection(OLBK_SERVER_PORT[1], OnlineBanking)
          print("Transfer from account {:>16} to account -------------------------".format(products["accounts"][int(account_sel)-1]))
          i = 1
          for account in products["accounts"]:
            print("({}) {:>16} $ {:>20,.02f}".format(i, account, float(clientOnlineBanking.getBalance(account))))
            i+= 1

          print("-----------------------------------------------------------------------------")
          print("")
          transportOnlineBanking.close()
          transfer_to = input("Account -----------------------------------------------------------------> ")
          amount      = input("Amount  -----------------------------------------------------------------> ")
          clientOnlineBanking,      transportOnlineBanking      = \
            createConnection(OLBK_SERVER_PORT[1], OnlineBanking)
          clientOnlineBanking.transferMoney(products["accounts"][int(account_sel)-1], products["accounts"][int(transfer_to)-1], float(amount))
          transportOnlineBanking.close() 

      elif opt == '3':
        os.system('clear')
        clientOnlineBanking,      transportOnlineBanking      = \
          createConnection(OLBK_SERVER_PORT[1], OnlineBanking)

        print("Select a card ---------------------------------------------------------------")
        i = 1
        for card in products["cards"]:
          print("({}) {:>16} $ {:>20,.02f}".format(i, account, float(clientOnlineBanking.getBalance(card))))
          i+= 1

        print("-----------------------------------------------------------------------------")
        print("")
        card_sel = input("Action ------------------------------------------------------------------> ")
        transportOnlineBanking.close()

      elif opt == 'X':
        session_active = False
        session_customerId = ''

if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
