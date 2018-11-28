#!/bin/bash

echo 'Killing all servers associated to the banking app...'
pkill -f HelloworldServer
pkill -f AuthServer
pkill -f CardManagementServer
pkill -f CustomerInformationServer
echo ''
echo 'Done!'
