local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.getLimit()
 local GenericObjectPool = require 'GenericObjectPool'
 local PaymentAuthorizationDBClient = require 'bank_PaymentAuthorizationDB'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.cardNumber)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 ngx.say(post.cardNumber)
 local client = GenericObjectPool:connection(PaymentAuthorizationDBClient, 'payment-authorization-db', 9090)
 
 local result = client:getLimit(post.cardNumber)
 GenericObjectPool:returnConnection(client)
 
 ngx.say(tostring(result))

end

return _M
