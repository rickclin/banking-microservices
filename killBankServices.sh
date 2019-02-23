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

echo ''
echo 'Done!'
