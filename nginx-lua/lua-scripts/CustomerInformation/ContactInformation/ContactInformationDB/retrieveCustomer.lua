local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.retrieveCustomer()
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

 local client = GenericObjectPool:connection(ContactInformationDBClient, 'contact-information-db', 9090)
 
 local result = client:retrieveCustomer(post.customerId)
 GenericObjectPool:returnConnection(client)

 ngx.say(result["firstName"])
 ngx.say(result["lastName"])
 ngx.say(result["homeNumber"])
 ngx.say(result["mobileNumber"])
 ngx.say(result["address"])

end

return _M
