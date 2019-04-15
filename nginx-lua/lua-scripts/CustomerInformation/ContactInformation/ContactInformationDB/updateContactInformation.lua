local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.updateContactInformation()
 local GenericObjectPool = require 'GenericObjectPool'
 local ContactInformationDBClient = require 'bank_ContactInformationDB'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.customerId)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 revisedInfo = {}

 if not _StrIsEmpty(post.revisedInfo_firstName) then
   revisedInfo["firstName"] = post.revisedInfo_firstName
 end

 if not _StrIsEmpty(post.revisedInfo_lastName) then
   revisedInfo["lastName"] = post.revisedInfo_lastName
 end 
 
 if not _StrIsEmpty(post.revisedInfo_homeNumber) then
   revisedInfo["homeNumber"] = post.revisedInfo_homeNumber
 end 
 
 if not _StrIsEmpty(post.revisedInfo_mobileNumber) then
   revisedInfo["mobileNumber"] = post.revisedInfo_mobileNumber
 end 
 
 if not _StrIsEmpty(post.revisedInfo_address) then
   revisedInfo["address"] = post.revisedInfo_address
 end
 
 local client = GenericObjectPool:connection(ContactInformationDBClient, 'contact-information-db', 9090)


 local result = client:updateContactInformation(post.customerId, revisedInfo)
 GenericObjectPool:returnConnection(client)

 ngx.say(result)

end

return _M
