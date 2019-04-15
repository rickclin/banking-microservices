local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.updateBalance()
 local GenericObjectPool = require 'GenericObjectPool'
 local AccountInformationDBClient = require 'bank_AccountInformationDB'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.accountNumber) or _StrIsEmpty(post.amount)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(AccountInformationDBClient, 'account-information-db', 9090)

 local result = client:updateBalance(post.accountNumber, post.amount)
 GenericObjectPool:returnConnection(client)
 
 ngx.say(result)

end

return _M
