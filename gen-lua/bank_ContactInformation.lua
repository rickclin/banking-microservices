--
-- Autogenerated by Thrift
--
-- DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
-- @generated
--

local Thrift = require "Thrift"
local TType = Thrift[1]
local TMessageType = Thrift[2]
local __TObject = Thrift[3]
local TApplicationException = Thrift[5]
local __TClient = Thrift[6]
local __TProcessor = Thrift[7]

-- HELPER FUNCTIONS AND STRUCTURES

local retrieveCustomer_args = __TObject:new{
  customerId
}

function retrieveCustomer_args:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 1 then
      if ftype == TType.STRING then
        self.customerId = iprot:readString()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function retrieveCustomer_args:write(oprot)
  oprot:writeStructBegin('retrieveCustomer_args')
  if self.customerId ~= nil then
    oprot:writeFieldBegin('customerId', TType.STRING, 1)
    oprot:writeString(self.customerId)
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

local retrieveCustomer_result = __TObject:new{
  success
}

function retrieveCustomer_result:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 0 then
      if ftype == TType.MAP then
        self.success = {}
        local _ktype79, _vtype80, _size78 = iprot:readMapBegin() 
        for _i=1,_size78 do
          local _key82 = iprot:readString()
          local _val83 = iprot:readString()
          self.success[_key82] = _val83
        end
        iprot:readMapEnd()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function retrieveCustomer_result:write(oprot)
  oprot:writeStructBegin('retrieveCustomer_result')
  if self.success ~= nil then
    oprot:writeFieldBegin('success', TType.MAP, 0)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.success))
    for kiter84,viter85 in pairs(self.success) do
      oprot:writeString(kiter84)
      oprot:writeString(viter85)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

local updateContactInformation_args = __TObject:new{
  customerId,
  revisedInfo
}

function updateContactInformation_args:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 1 then
      if ftype == TType.STRING then
        self.customerId = iprot:readString()
      else
        iprot:skip(ftype)
      end
    elseif fid == 2 then
      if ftype == TType.MAP then
        self.revisedInfo = {}
        local _ktype87, _vtype88, _size86 = iprot:readMapBegin() 
        for _i=1,_size86 do
          local _key90 = iprot:readString()
          local _val91 = iprot:readString()
          self.revisedInfo[_key90] = _val91
        end
        iprot:readMapEnd()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function updateContactInformation_args:write(oprot)
  oprot:writeStructBegin('updateContactInformation_args')
  if self.customerId ~= nil then
    oprot:writeFieldBegin('customerId', TType.STRING, 1)
    oprot:writeString(self.customerId)
    oprot:writeFieldEnd()
  end
  if self.revisedInfo ~= nil then
    oprot:writeFieldBegin('revisedInfo', TType.MAP, 2)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.revisedInfo))
    for kiter92,viter93 in pairs(self.revisedInfo) do
      oprot:writeString(kiter92)
      oprot:writeString(viter93)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

local updateContactInformation_result = __TObject:new{
  success
}

function updateContactInformation_result:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 0 then
      if ftype == TType.BOOL then
        self.success = iprot:readBool()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function updateContactInformation_result:write(oprot)
  oprot:writeStructBegin('updateContactInformation_result')
  if self.success ~= nil then
    oprot:writeFieldBegin('success', TType.BOOL, 0)
    oprot:writeBool(self.success)
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

-- CLIENT AND PUBLIC FUNCTIONS

local ContactInformationClient = __TObject.new(__TClient, {
  __type = 'ContactInformationClient'
})

function ContactInformationClient:retrieveCustomer(customerId)
  self:send_retrieveCustomer(customerId)
  return self:recv_retrieveCustomer(customerId)
end

function ContactInformationClient:send_retrieveCustomer(customerId)
  self.oprot:writeMessageBegin('retrieveCustomer', TMessageType.CALL, self._seqid)
  local args = retrieveCustomer_args:new{}
  args.customerId = customerId
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function ContactInformationClient:recv_retrieveCustomer(customerId)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = retrieveCustomer_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
  if result.success ~= nil then
    return result.success
  end
  error(TApplicationException:new{errorCode = TApplicationException.MISSING_RESULT})
end

function ContactInformationClient:updateContactInformation(customerId, revisedInfo)
  self:send_updateContactInformation(customerId, revisedInfo)
  return self:recv_updateContactInformation(customerId, revisedInfo)
end

function ContactInformationClient:send_updateContactInformation(customerId, revisedInfo)
  self.oprot:writeMessageBegin('updateContactInformation', TMessageType.CALL, self._seqid)
  local args = updateContactInformation_args:new{}
  args.customerId = customerId
  args.revisedInfo = revisedInfo
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function ContactInformationClient:recv_updateContactInformation(customerId, revisedInfo)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = updateContactInformation_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
  if result.success ~= nil then
    return result.success
  end
  error(TApplicationException:new{errorCode = TApplicationException.MISSING_RESULT})
end
local ContactInformationIface = __TObject:new{
  __type = 'ContactInformationIface'
}


local ContactInformationProcessor = __TObject.new(__TProcessor
, {
 __type = 'ContactInformationProcessor'
})

function ContactInformationProcessor:process(iprot, oprot, server_ctx)
  local name, mtype, seqid = iprot:readMessageBegin()
  local func_name = 'process_' .. name
  if not self[func_name] or ttype(self[func_name]) ~= 'function' then
    iprot:skip(TType.STRUCT)
    iprot:readMessageEnd()
    x = TApplicationException:new{
      errorCode = TApplicationException.UNKNOWN_METHOD
    }
    oprot:writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
    x:write(oprot)
    oprot:writeMessageEnd()
    oprot.trans:flush()
  else
    self[func_name](self, seqid, iprot, oprot, server_ctx)
  end
end

function ContactInformationProcessor:process_retrieveCustomer(seqid, iprot, oprot, server_ctx)
  local args = retrieveCustomer_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = retrieveCustomer_result:new{}
  local status, res = pcall(self.handler.retrieveCustomer, self.handler, args.customerId)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  else
    result.success = res
  end
  oprot:writeMessageBegin('retrieveCustomer', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

function ContactInformationProcessor:process_updateContactInformation(seqid, iprot, oprot, server_ctx)
  local args = updateContactInformation_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = updateContactInformation_result:new{}
  local status, res = pcall(self.handler.updateContactInformation, self.handler, args.customerId, args.revisedInfo)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  else
    result.success = res
  end
  oprot:writeMessageBegin('updateContactInformation', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

return ContactInformationClient
