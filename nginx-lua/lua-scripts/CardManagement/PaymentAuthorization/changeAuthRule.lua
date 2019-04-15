local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.changeAuthRule()
 local GenericObjectPool = require 'GenericObjectPool'
 local PaymentAuthorizationClient = require 'bank_PaymentAuthorization'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.cardNumber) or _StrIsEmpty(post.newAmount)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(PaymentAuthorizationClient, 'payment-authorization', 9090)
 
 local result = client:changeAuthRule(post.cardNumber, post.newAmount)
 GenericObjectPool:returnConnection(client)

 ngx.say(result)

end

return _M
