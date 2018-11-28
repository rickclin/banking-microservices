#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import glob
import sys
sys.path.append('gen-py')

from thrift import Thrift
from bank import CardManagement

from datetime import datetime

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

card_db = ['1234123412341234']
auth_rule_db = {'1234123412341234' : 300}
tranx_db = {'1234123412341234' : []}

class CardManagementHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def authorizePayment(self, cardNumber, amount):
      auth = False
      limit = auth_rule_db[cardNumber]
      resp = str(amount) + ' exceeds the transaction limit ' + str(limit)

      if amount <= limit:
        timestamp = str(datetime.now())
        tranx_db[cardNumber].append(str(amount) + ', ' + timestamp)
        auth = True
        resp = str(amount) + ' posted to ' + cardNumber[-4:] + \
               ' at ' + timestamp

      return resp

    def getTransactionHistory(self, cardNumber):
      history = tranx_db[cardNumber]
      return history
      #for entry in history:
      #  print(entry)
    
    def getCardNumber(self):
      return card_db[0]

if __name__ == '__main__':
    handler = CardManagementHandler()
    processor = CardManagement.Processor(handler)
    transport = TSocket.TServerSocket(host='localhost', port=19093)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('Card Management done.')
