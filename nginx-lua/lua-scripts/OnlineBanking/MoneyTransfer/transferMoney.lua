local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.transferMoney()
 local GenericObjectPool = require 'GenericObjectPool'
 local MoneyTransferClient = require 'bank_MoneyTransfer'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.fromAccount) or _StrIsEmpty(post.toAccount) or _StrIsEmpty(post.amount)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(MoneyTransferClient, 'money-transfer', 9090)

 local result = client:transferMoney(post.fromAccount, post.toAccount, post.amount)
 GenericObjectPool:returnConnection(client)
 
 ngx.say(result)

end

return _M
