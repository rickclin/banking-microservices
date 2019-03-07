#!/bin/bash

./killBankServices.sh

echo 'Starting all associated servers for the banking app'

echo '[localhost:19090] Starting HelloworldServer...'
python3 HelloworldServer.py &
#echo ''

# echo 'Starting AuthServer...'
# python3 AuthServer.py &
# #echo ''
# 

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
