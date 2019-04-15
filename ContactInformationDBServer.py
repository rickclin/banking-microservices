#!/usr/bin/env python

import glob
import sys
import datetime
import random
import string

sys.path.append('gen-py')

from thrift           import Thrift
from bank             import ContactInformationDB

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol  import TBinaryProtocol
from thrift.server    import TServer

SERVER_PORT = ('0.0.0.0', 9090)
FIRST =   {'customerId':'firstName'}
LAST =    {'customerId':'lastName'}
HOME =    {'customerId':'homeNumber'}
MOBILE =  {'customerId':'mobileNumber'}
ADDRESS = {'customerId':'address'}


class ContactInformationDBHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def retrieveCustomer(self, customerId):
      contact = {}
      contact['firstName']    = FIRST[customerId]   if customerId in FIRST.keys() else ''
      contact['lastName']     = LAST[customerId]    if customerId in LAST.keys() else ''
      contact['homeNumber']   = HOME[customerId]    if customerId in HOME.keys() else ''
      contact['mobileNumber'] = MOBILE[customerId]  if customerId in MOBILE.keys() else ''
      contact['address']      = ADDRESS[customerId] if customerId in ADDRESS.keys() else ''
      return contact

    def updateContactInformation(self, customerId, revisedInfo):
      if 'firstName' in revisedInfo.keys():
        FIRST[customerId]   = revisedInfo['firstName']
      if 'lastName' in revisedInfo.keys():
        LAST[customerId]    = revisedInfo['lastName'] 
      if 'homeNumber' in revisedInfo.keys():
        HOME[customerId]    = revisedInfo['homeNumber'] 
      if 'mobileNumber' in revisedInfo.keys():
        MOBILE[customerId]  = revisedInfo['mobileNumber'] 
      if 'address' in revisedInfo.keys():
        ADDRESS[customerId] = revisedInfo['address']

      return True


if __name__ == '__main__':
    handler = ContactInformationDBHandler()
    processor = ContactInformationDB.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' Starting the ContactInformationDBServer...')
    server.serve()
    print('[' + SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + ']' + ' ContactInformationDBServer done.')
