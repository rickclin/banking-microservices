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
import datetime

sys.path.append('gen-py')

from thrift import Thrift
from bank import ContactInformation

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

SERVER_PORT = ('localhost', )

class PaymentAuthorization:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

if __name__ == '__main__':
    handler = RegisteredProductsHandler()
    processor = RegisteredProducts.Processor(handler)
    transport = TSocket.TServerSocket(host=SERVER_PORT[0], port=SERVER_PORT[1])
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print(SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + 'Starting the ContactInformationServer...')
    server.serve()
    print(SERVER_PORT[0] + ':' + str(SERVER_PORT[1]) + 'ContactInformationServer done.')
