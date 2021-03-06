#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def retrieveCustomer(self, customerId):
        """
        Parameters:
         - customerId
        """
        pass

    def updateContactInformation(self, customerId, revisedInfo):
        """
        Parameters:
         - customerId
         - revisedInfo
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def retrieveCustomer(self, customerId):
        """
        Parameters:
         - customerId
        """
        self.send_retrieveCustomer(customerId)
        return self.recv_retrieveCustomer()

    def send_retrieveCustomer(self, customerId):
        self._oprot.writeMessageBegin('retrieveCustomer', TMessageType.CALL, self._seqid)
        args = retrieveCustomer_args()
        args.customerId = customerId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_retrieveCustomer(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = retrieveCustomer_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "retrieveCustomer failed: unknown result")

    def updateContactInformation(self, customerId, revisedInfo):
        """
        Parameters:
         - customerId
         - revisedInfo
        """
        self.send_updateContactInformation(customerId, revisedInfo)
        return self.recv_updateContactInformation()

    def send_updateContactInformation(self, customerId, revisedInfo):
        self._oprot.writeMessageBegin('updateContactInformation', TMessageType.CALL, self._seqid)
        args = updateContactInformation_args()
        args.customerId = customerId
        args.revisedInfo = revisedInfo
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateContactInformation(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateContactInformation_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateContactInformation failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["retrieveCustomer"] = Processor.process_retrieveCustomer
        self._processMap["updateContactInformation"] = Processor.process_updateContactInformation

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_retrieveCustomer(self, seqid, iprot, oprot):
        args = retrieveCustomer_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = retrieveCustomer_result()
        try:
            result.success = self._handler.retrieveCustomer(args.customerId)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("retrieveCustomer", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateContactInformation(self, seqid, iprot, oprot):
        args = updateContactInformation_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateContactInformation_result()
        try:
            result.success = self._handler.updateContactInformation(args.customerId, args.revisedInfo)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("updateContactInformation", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class retrieveCustomer_args(object):
    """
    Attributes:
     - customerId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'customerId', 'UTF8', None, ),  # 1
    )

    def __init__(self, customerId=None,):
        self.customerId = customerId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.customerId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('retrieveCustomer_args')
        if self.customerId is not None:
            oprot.writeFieldBegin('customerId', TType.STRING, 1)
            oprot.writeString(self.customerId.encode('utf-8') if sys.version_info[0] == 2 else self.customerId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class retrieveCustomer_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype109, _vtype110, _size108) = iprot.readMapBegin()
                    for _i112 in range(_size108):
                        _key113 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val114 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success[_key113] = _val114
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('retrieveCustomer_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.success))
            for kiter115, viter116 in self.success.items():
                oprot.writeString(kiter115.encode('utf-8') if sys.version_info[0] == 2 else kiter115)
                oprot.writeString(viter116.encode('utf-8') if sys.version_info[0] == 2 else viter116)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class updateContactInformation_args(object):
    """
    Attributes:
     - customerId
     - revisedInfo
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'customerId', 'UTF8', None, ),  # 1
        (2, TType.MAP, 'revisedInfo', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
    )

    def __init__(self, customerId=None, revisedInfo=None,):
        self.customerId = customerId
        self.revisedInfo = revisedInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.customerId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.revisedInfo = {}
                    (_ktype118, _vtype119, _size117) = iprot.readMapBegin()
                    for _i121 in range(_size117):
                        _key122 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val123 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.revisedInfo[_key122] = _val123
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('updateContactInformation_args')
        if self.customerId is not None:
            oprot.writeFieldBegin('customerId', TType.STRING, 1)
            oprot.writeString(self.customerId.encode('utf-8') if sys.version_info[0] == 2 else self.customerId)
            oprot.writeFieldEnd()
        if self.revisedInfo is not None:
            oprot.writeFieldBegin('revisedInfo', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.revisedInfo))
            for kiter124, viter125 in self.revisedInfo.items():
                oprot.writeString(kiter124.encode('utf-8') if sys.version_info[0] == 2 else kiter124)
                oprot.writeString(viter125.encode('utf-8') if sys.version_info[0] == 2 else viter125)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class updateContactInformation_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.BOOL, 'success', None, None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('updateContactInformation_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
