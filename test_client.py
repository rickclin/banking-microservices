#!/usr/bin/python3
# choose which test(s) to run

TEST_CARD_MANAGEMENT      = False
TEST_CUSTOMER_INFORMATION = True
TEST_ONLINE_BANKING       = True

import sys
sys.path.append('gen-py')

from bank             import HelloworldService      # 19090

if TEST_CARD_MANAGEMENT:
  from bank             import CardManagement         # 19093
  from bank             import CustomerInformation    # 19094
  from bank             import PaymentAuthorization   # 19096
  from bank             import PaymentAuthorizationDB # 19098
  from bank             import TransactionHistory     # 19095 
  from bank             import TransactionHistoryDB   # 19097

if TEST_CUSTOMER_INFORMATION:
  from bank             import RegisteredProducts     # 19100
  from bank             import RegisteredProductsDB   # 19102
  from bank             import ContactInformation     # 19099
  from bank             import ContactInformationDB   # 19101
  from bank             import CustomerInformation    # 19094

if TEST_ONLINE_BANKING:
  from bank             import AccountInformationDB   # 19106
  from bank             import AccountInformation     # 19104
  from bank             import MoneyTransfer          # 19105
  from bank             import OnlineBanking          # 19103

from thrift           import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol

import time
import getpass
import random
import string

def createConnection(container, service):
    transport = TSocket.TSocket(container, 9090)
    transport = TTransport.TFramedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = service.Client(protocol)
    transport.open()
    return client, transport

def main():
  # Make socket
  #client,         transport         = createConnection(19090, HelloworldService) 
  #print("connections opened!")  
  # verify servers are up
  #res = client.getHelloworld()
  #print(res)
  #transport.close() 

  if TEST_CARD_MANAGEMENT:
    clientCard,     transportCard     = createConnection('card-management',          CardManagement) 
    clientAuth,     transportAuth     = createConnection('payment-authorization',    PaymentAuthorization) 
    clientAuthDB,   transportAuthDB   = createConnection('payment-authorization-db', PaymentAuthorizationDB) 
    clientTranx,    transportTranx    = createConnection('transaction-history',      TransactionHistory) 
    clientTranxDB,  transportTranxDB  = createConnection('transaction-history-db',   TransactionHistoryDB)

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
    print('[TEST] Payment Authorization Server successfully tested!')
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
    print('[TEST] Transactions by card ending in 0000: all between 02-27 and 03-01')
    match = clientTranx.filterTransactions('0000000000000000', 0, '2019-02-27, 2019-03-02', '', '', '')
    print('[TEST] ' + str(len(match)) + ' matching transactions: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')
    print('[TEST] Transactions by card ending in 0000: all containing \'Z\' in their descriptions')
    match = clientTranx.filterTransactions('0000000000000000', 0, '', '', '', 'Z')
    print('[TEST] ' + str(len(match)) + ' matching transactions: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')
    print('[TEST] Transactions by card ending in 0000: all between $10-$50, swipe entered, from 2/27-3/01')
    match = clientTranx.filterTransactions('0000000000000000', 0, '2019-02-27, 2019-03-02', '10, 50', 'swipe', '')
    print('[TEST] ' + str(len(match)) + ' matching transactions: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')
    print('[TEST] Transactions by card ending in 0000: first 5 between $10-$50, swipe entered, from 2/27-3/01')
    match = clientTranx.filterTransactions('0000000000000000', 5, '2019-02-27, 2019-03-02', '10, 50', 'swipe', '')
    print('[TEST] ' + str(len(match)) + ' matching transactions: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')
    
    initial_log = clientTranx.getTransactionLog('0000000000000000')
    print('[TEST] ' + str(len(initial_log)) + ' entries already exist!')
    print('[TEST] Inserting more transactions with transaction history server...')
    for i in range(0,200):
      digit = random.randint(1, 100)
      dec   = random.randint(1, 100) / 100
      amount= digit + dec
      entry = ['chip', 'swipe', 'online'][digit%3]
      des = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
      clientTranx.insertTransaction('0000000000000000', amount, entry, des)
      time.sleep(dec*0.05)
    print('[TEST] Displays the complete transaction log')
    update_log = clientTranx.getTransactionLog('0000000000000000')
    print('\n'.join(update_log))
    transportTranx.close()
    print('[TEST] ' + str(len(update_log)) + ' entries are now in the card history!')
    input('[PAUSE] Press Return to continue...')
    
    # communicating with Card Management server
    # post
    print('[TEST] posting transactions from level-1 Card Mgmt server')
    assert clientCard.postTransaction('0000000000000000', '[CARD MGMT POSTED] transaction X', 299.50, 'online') == True
    assert clientCard.postTransaction('0000000000000000', '[CARD MGMT POSTED] transaction Y', 1000.00, 'online') == False
    print('[TEST] 1 transaction posted, 1 transaction declined (exceeds card limit)')
    input('[PAUSE] Press Return to continue...')

    # get
    print('[TEST] getting transactions from level-1 Card Mgmt server')
    update_log = clientCard.getTransactions('0000000000000000', 0, '', '', '')
    print('\n'.join(update_log))
    print('[TEST] ' + str(len(update_log)) + ' entries are now in the card history!')
    input('[PAUSE] Press Return to continue...')

    # search
    print('[TEST] searching transactionsn from level-1 Card Mgmt server')
    match = clientCard.searchTransactions('0000000000000000', 'CARD MGMT')
    print('[TEST] ' + str(len(match)) + ' matching transactions posted from Card Mgmt server: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')

    # change limit
    print('[TEST] modifying authorization rule from level-1 Card Mgmt server')
    ack = clientCard.changeAuthorizationRule('0000000000000000', 25.00)
    print('[TEST] auth rule changed to 25.00 for card ending in 0000' if ack else '[TEST] unable to change auth rule')
    ack = clientCard.postTransaction('0000000000000000', '[CARD MGMT POSTED] transaction Z', 299.50, 'online')
    print('[TEST] 299.50 posted' if ack else '[TEST] 299.50 declined')
    ack = clientCard.postTransaction('0000000000000000', '[CARD MGMT POSTED] transaction A', 9.50, 'online')
    print('[TEST] 9.50 posted' if ack else '[TEST] 9.50 declined')
    match = clientCard.searchTransactions('0000000000000000', 'CARD MGMT')
    print('[TEST] ' + str(len(match)) + ' matching transactions posted from Card Mgmt server: ')
    print('\n'.join(match))
    input('[PAUSE] Press Return to continue')

    transportCard.close()
  
  if TEST_CUSTOMER_INFORMATION:
    clientProdDB,   transportProdDB   = createConnection('registered-products-db', RegisteredProductsDB)
    clientProd,     transportProd     = createConnection('registered-products',    RegisteredProducts)
    clientContactDB,transportContactDB= createConnection('contact-information-db', ContactInformationDB)
    clientContact,  transportContact  = createConnection('contact-information',    ContactInformation)
    clientCustomer, transportCustomer = createConnection('customer-information',   CustomerInformation)

    # communicating with Registered Products DB Server
    print('[TEST] inserting new cards into the DB')
    for x in range(0,5):
      newCardNumber = clientProdDB.addCard('accountholder0')
      print('[TEST] card ' + newCardNumber + ' created for accountholder0')
    
    print('[TEST] cards available for accountholder0')
    print('\n'.join(clientProdDB.getCardNumbers('accountholder0')))

    print('[TEST] inserting new accounts into the DB')
    for x in range(0,5):
      newAccountNumber = clientProdDB.addAccount('accountholder0')
      print('[TEST] account ' + newAccountNumber + ' created for accountholder0')
    
    print('[TEST] accounts available for accountholder0')
    print('\n'.join(clientProdDB.getAccountNumbers('accountholder0')))
    input('[PAUSE] Press Return to continue')

    transportProdDB.close()
    
    # communicating with Registered Products Server
    print('[TEST] inserting new cards/accounts into the DB with registered products server')
    for x in range(0,5):
      newCardNumber    = clientProd.addCard('accountholder1')
      newAccountNumber = clientProd.addAccount('accountholder1')
      print('[TEST] card ' + newCardNumber + ' created for accountholder1')
      print('[TEST] account ' + newAccountNumber + ' created for accountholder1')

    customerProducts = clientProd.getRegisteredProducts('accountholder1')
    print('[TEST] accountholder1 has the following cards available:')
    print('\n'.join(customerProducts['cards']))
    print('[TEST] accountholder1 has the following accounts available:')
    print('\n'.join(customerProducts['accounts']))
    input('[PAUSE] Press Return to continue')

    transportProd.close()
    
    #communicating with contact information DB server
    print('[TEST] inserting new customer contacts into the DB')
    accountholder0_Info = {'firstName':'John', 'lastName':'Adams', 'homeNumber':'2068887777', 'mobileNumber':'4253232334', 'address':'100 W PINE SEATTLE WA 98104'}
    accountholder1_Info = {'firstName':'Alice', 'lastName':'Keys', 'homeNumber':'6077778888', 'mobileNumber':'9175454556', 'address':'7777 NY-13 ITHACA NY 14850'}
    assert clientContactDB.updateContactInformation('accountholder0', accountholder0_Info) == True
    assert clientContactDB.updateContactInformation('accountholder1', accountholder1_Info) == True
    print('[TEST] John\'s and Alice\'s information is now in the DB!')
    print('[TEST] retrieving their contact information and verifying it against the original one')
    assert clientContactDB.retrieveCustomer('accountholder0') == accountholder0_Info
    assert clientContactDB.retrieveCustomer('accountholder1') == accountholder1_Info
    print('[TEST] information matched!')
    print('[TEST] John\'s information:')
    print(clientContactDB.retrieveCustomer('accountholder0'))
    print('[TEST] Alice\'s information:')
    print(clientContactDB.retrieveCustomer('accountholder1'))
    input('[PAUSE] Press Return to continue')

    transportContactDB.close()

    #communicating with contact information server
    print('[TEST] inserting new customer contacts into the DB from contact information server')
    accountholder2_Info = {'firstName':'Bob', 'lastName':'Cray', 'homeNumber':'9890020002', 'mobileNumber':'8880657799', 'address':'23 BROADWAY N EL PASO TX 79901'}
    accountholder3_Info = {'firstName':'Eve', 'lastName':'Finsky', 'homeNumber':'3669083465', 'mobileNumber':'74513235467', 'address':'11533 S DAKOTA AVE FARGO ND 58047'}
    accountholder0_Info = {'firstName':'John', 'lastName':'Adams', 'homeNumber':'2068887777', 'mobileNumber':'4253232334', 'address':'506 NE 124TH ST BELLEVUE WA 98005'}
    accountholder1_Info = {'firstName':'Alice', 'lastName':'Keys', 'homeNumber':'6077778888', 'mobileNumber':'9175454556', 'address':'1 DOITMY WAY ITHACA NY 14850'}
    assert clientContact.updateContactInformation('accountholder2', accountholder2_Info) == True
    assert clientContact.updateContactInformation('accountholder3', accountholder3_Info) == True
    assert clientContact.updateContactInformation('accountholder0', accountholder0_Info) == True
    assert clientContact.updateContactInformation('accountholder1', accountholder1_Info) == True
    print('[TEST] Bob\'s and Eve\'s information is now in the DB!')
    print('[TEST] John and Alice recently moved. Updating their addresses')
    print('[TEST] retrieving their contact information and verifying it against the original one')
    assert clientContact.retrieveCustomer('accountholder0') == accountholder0_Info
    assert clientContact.retrieveCustomer('accountholder1') == accountholder1_Info
    assert clientContact.retrieveCustomer('accountholder2') == accountholder2_Info
    assert clientContact.retrieveCustomer('accountholder3') == accountholder3_Info
    print('[TEST] information matched!')
    print('[TEST] John\'s new information:')
    print(clientContact.retrieveCustomer('accountholder0'))
    print('[TEST] Alice\'s new information:')
    print(clientContact.retrieveCustomer('accountholder1'))
    print('[TEST] Bob\'s information:')
    print(clientContact.retrieveCustomer('accountholder2'))
    print('[TEST] Eve\'s information:')
    print(clientContact.retrieveCustomer('accountholder3'))
    input('[PAUSE] Press Return to continue')

    transportContact.close()

    # communicating with customer information server
    print('[TEST] Read contact information from the customer information server')
    print('Verifying the information against the original information')
    assert clientCustomer.retrieveContactInformation('accountholder0') == accountholder0_Info
    assert clientCustomer.retrieveContactInformation('accountholder1') == accountholder1_Info
    assert clientCustomer.retrieveContactInformation('accountholder2') == accountholder2_Info
    assert clientCustomer.retrieveContactInformation('accountholder3') == accountholder3_Info

    print('[TEST] Update contact information from the customer information server')
    clientCustomer.updateContactInformation('accountholder1', {'lastName':'Adams'})
    clientCustomer.updateContactInformation('accountholder3', {'lastName':'Cray'})
    assert clientCustomer.retrieveContactInformation('accountholder1')['lastName'] == 'Adams'
    assert clientCustomer.retrieveContactInformation('accountholder3')['lastName'] == 'Cray'

    print('[TEST] Security question check from contact information server')
    assert clientCustomer.verifyContactInformation('accountholder0', 'firstName', 'John')           == True
    assert clientCustomer.verifyContactInformation('accountholder0', 'homeNumber', '2068887777')    == True
    assert clientCustomer.verifyContactInformation('accountholder0', 'mobileNumber', '4253232334')  == True
    assert clientCustomer.verifyContactInformation('accountholder2', 'firstName', 'John')           == False
    assert clientCustomer.verifyContactInformation('accountholder2', 'homeNumber', '2068887777')    == False
    assert clientCustomer.verifyContactInformation('accountholder2', 'mobileNumber', '8880667799')  == False

    print('[TEST] Getting a list of registered products')
    print('Verifying accountholder1\'s registered products...')
    assert clientCustomer.getRegisteredProducts('accountholder1') == customerProducts

    print('[TEST] retrieve only account numbers of an account holder')
    print('Verifying accountholder1\'s account numbers...')
    assert clientCustomer.getAccountNumbers('accountholder1') == customerProducts['accounts']

    print('[TEST] retrieve only card numbers of an account holder')
    print('Verifying accountholder1\'s card numbers...')
    assert clientCustomer.getCardNumbers('accountholder1') == customerProducts['cards']

    print('[TEST] create some new accounts')
    newAccount = clientCustomer.newAccount('accountholder0')
    assert newAccount in clientCustomer.getAccountNumbers('accountholder0')

    print('[TEST] create some new cards')
    newCard = clientCustomer.newCard('accountholder0')
    assert newCard in clientCustomer.getCardNumbers('accountholder0')

    input('[PAUSE] Press Return to continue')
    
    transportCustomer.close()

  if TEST_ONLINE_BANKING:
    clientAcctInfoDB, transportAcctInfoDB   = createConnection('account-information-db', AccountInformationDB)
    clientAcctInfo,   transportAcctInfo     = createConnection('account-information',    AccountInformation)
    clientMoneyTx,    transportMoneyTx      = createConnection('money-transfer',         MoneyTransfer)
    clientOnlineBank, transportOnlineBank   = createConnection('online-banking',         OnlineBanking)

    print('[TEST] Testing account information simulated DB')
    print('[TEST] Getting the balance of card account ending in 0000')
    assert clientAcctInfoDB.getBalance('0000000000000000') == str(50.00)
    assert clientAcctInfoDB.getBalance('0000000000000001') == 'n/a'
    input('[PAUSE] Press Return to continue')

    print('[TEST] Updating the balances...')
    assert clientAcctInfoDB.updateBalance('0000000000000000', '5.50') == str(55.50)
    assert clientAcctInfoDB.updateBalance('0000000000000001', '0.01') == 'n/a'
    input('[PAUSE] Press Return to continue')
    
    print('[TEST] Adding a new account to the DB...')
    assert clientAcctInfoDB.addAccount('0000000000000000') == False
    assert clientAcctInfoDB.addAccount('0000000000000001') == True
    assert clientAcctInfoDB.getBalance('0000000000000001') == str(0.00)
    print(clientAcctInfoDB.getBalance('0000000000000001'))
    input('[PAUSE] Press Return to continue')
    
    transportAcctInfoDB.close()

    print('[TEST] Testing account information server...')
    print('[TEST] Getting the balance of card account ending in 0000')
    assert clientAcctInfo.getBalance('0000000000000000') == str(55.50)
    assert clientAcctInfo.getBalance('0000000000000001') == str(0.00)
    assert clientAcctInfo.getBalance('1000000000000000') == 'n/a'
    print('[TEST] No problem reading account balances from account information server')
    input('[PAUSE] Press Return to continue')
    
    print('[TEST] changing the balances...')
    assert clientAcctInfo.updateBalance('0000000000000000', '-5.50') == str(50.00)
    assert clientAcctInfo.updateBalance('0000000000000001', '-1.00') == str(-1.00)
    assert clientAcctInfo.updateBalance('1000000000000000', '1.00' ) == 'n/a'
    print('[TEST] no problem changing the balances from account information server')
    input('[PAUSE] Press Return to continue')
  
    transportAcctInfo.close()

    print('[TEST] testing money transfer server...')
    assert clientMoneyTx.transferMoney('0000000000000000', '0000000000000001', '5.00') == True
    # assert clientAcctInfo.getBalance('0000000000000000') == str(45.00)
    # assert clientAcctInfo.getBalance('0000000000000000') == str(4.00)
    assert clientMoneyTx.transferMoney('0000000000000001', '0000000000000000', '50.00') == False
    # assert clientAcctInfo.getBalance('0000000000000000') == str(45.00)
    # assert clientAcctInfo.getBalance('0000000000000000') == str(4.00)
    assert clientMoneyTx.transferMoney('1000000000000000', '0000000000000000', '5.00') == False
    assert clientMoneyTx.transferMoney('0000000000000000', '1000000000000000', '5.00') == False
    # assert clientAcctInfo.getBalance('0000000000000000') == str(45.00)
    print('[TEST] no issue was found while transferring money')
    input('[PAUSE] Press Return to continue')

    transportMoneyTx.close()

    print('[TEST] testing online banking main server')
    print('[TEST] checking the balances...')
    assert clientOnlineBank.getBalance('0000000000000000') == str(45.00)
    assert clientOnlineBank.getBalance('0000000000000001') == str(4.00)
    assert clientOnlineBank.getBalance('0000000000000002') == 'n/a'
    input('[PAUSE] Press Return to continue')

    print('[TEST] transferring money')
    assert clientOnlineBank.transferMoney('0000000000000000', '0000000000000001', '5.00') == True
    assert clientOnlineBank.getBalance('0000000000000000') == str(40.00)
    assert clientOnlineBank.getBalance('0000000000000001') == str(9.00)
    assert clientOnlineBank.transferMoney('0000000000000001', '0000000000000000', '50.00') == False
    assert clientOnlineBank.getBalance('0000000000000000') == str(40.00)
    assert clientOnlineBank.getBalance('0000000000000001') == str(9.00)
    assert clientOnlineBank.transferMoney('1000000000000000', '0000000000000000', '5.00') == False
    assert clientOnlineBank.transferMoney('0000000000000000', '1000000000000000', '5.00') == False
    assert clientOnlineBank.getBalance('0000000000000000') == str(40.00)
    print('[TEST] no issue was found while transferring money')
    input('[PAUSE] Press Return to continue')

    transportOnlineBank.close()


if __name__ == '__main__':
  try:
    main()
  except Thrift.TException as tx:
    print('%s' % tx.message)
