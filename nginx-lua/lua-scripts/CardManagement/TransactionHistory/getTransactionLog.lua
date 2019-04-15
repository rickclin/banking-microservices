local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.getTransactionLog()
 local GenericObjectPool = require 'GenericObjectPool'
 local TransactionHistoryClient = require 'bank_TransactionHistory'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.cardNumber)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(TransactionHistoryClient, 'transaction-history', 9090)

 local result = client:getTransactionLog(post.cardNumber)
 GenericObjectPool:returnConnection(client)

 ngx.say(table.concat(result, ","))

end

return _M
