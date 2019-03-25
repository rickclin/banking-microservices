#!/bin/bash

./killBankServices.sh

echo 'Starting all associated servers for the banking app'

echo '[localhost:19090] Starting HelloworldServer...'
python3 HelloworldServer.py &
#echo ''

echo '[localhost:19092] Starting AuthServer...'
python3 AuthServer.py &
#echo ''

echo '[localhost:19093] Starting CardManagementServer...'
python3 CardManagementServer.py &
#echo ''

echo '[localhost:19094] Starting CustomerInformationServer...'
python3 CustomerInformationServer.py &
#echo ''

echo '[localhost:19095] Starting TransactionHistoryServer...'
python3 TransactionHistoryServer.py &
#echo ''

echo '[localhost:19096] Starting PaymentAuthorizationServer...'
python3 PaymentAuthorizationServer.py &
#echo ''

echo '[localhost:19097] Starting TransactionHistoryDB...'
python3 TransactionHistoryDBServer.py &
#echo ''

echo '[localhost:19098] Starting PaymentAuthorizationDB...'
python3 PaymentAuthorizationDBServer.py &
#echo ''

echo '[localhost:19199] Starting ContactInformationServer...'
python3 ContactInformationServer.py &
#echo ''

echo '[localhost:19100] Starting RegisteredProductsServer...'
python3 RegisteredProductsServer.py &
#echo ''

echo '[localhost:19101] Starting ContactInformationDB...'
python3 ContactInformationDBServer.py &
#echo ''

echo '[localhost:19102] Starting RegisteredProductsDB...'
python3 RegisteredProductsDBServer.py &
#echo ''

echo '[localhost:19103] Starting OnlineBankingServer...'
python3 OnlineBankingServer.py &
#echo ''

echo '[localhost:19104] Starting AccountInformationServer...'
python3 AccountInformationServer.py &
#echo ''

echo '[localhost:19105] Starting MoneyTransferServer...'
python3 MoneyTransferServer.py &
#echo ''

echo '[localhost:19106] Starting AccountInformationDB...'
python3 AccountInformationDBServer.py &
#echo ''
