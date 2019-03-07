#!/bin/bash

echo 'Killing all servers associated to the banking app...'
pkill -f 'python3 HelloworldServer'
pkill -f 'python3 AuthServer'
pkill -f 'python3 CardManagementServer'
pkill -f 'python3 CustomerInformationServer'
pkill -f 'python3 PaymentAuthorizationServer'
pkill -f 'python3 PaymentAuthorizationDBServer'
pkill -f 'python3 TransactionHistoryServer'
pkill -f 'python3 TransactionHistoryDBServer'
pkill -f 'python3 RegisteredProductsServer'
pkill -f 'python3 RegisteredProductsDBServer'
pkill -f 'python3 ContactInformationServer'
pkill -f 'python3 ContactInformationDBServer'

echo ''
echo 'Done!'
