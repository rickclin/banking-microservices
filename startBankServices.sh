#!/bin/bash

echo 'Starting all associated servers for the banking app'

echo 'Starting HelloworldServer...'
python HelloworldServer.py &
echo ''

echo 'Starting AuthServer...'
python AuthServer.py &
echo ''

echo 'Starting CardManagementServer...'
python CardManagementServer.py &
echo ''

echo 'Starting CustomerInformationServer...'
python CustomerInformationServer.py & 
echo ''
