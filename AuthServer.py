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
#sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from thrift import Thrift
from bank import AuthenticateService
from hashlib import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

user_db = {'ricklin' : '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',
           'user'    : 'c73ba2982c55b7ead0e4098a92f722bdb3a3b3d8'
          }

class AuthenticateHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def authenticate(self, user, password):
        digest = sha1(password).hexdigest() 
        print(password)
        print(digest)
        print(user_db[user])
        
        return user_db[user] == digest

if __name__ == '__main__':
    handler = AuthenticateHandler()
    processor = AuthenticateService.Processor(handler)
    transport = TSocket.TServerSocket(host='localhost', port=19092)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    print('Starting the Auth server...')
    server.serve()
    print('Auth done.')
