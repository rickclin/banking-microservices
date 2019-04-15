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

 if (_StrIsEmpty(post.cardNumber) or _StrIsEmpty(post.numOfResults) or
     _StrIsEmpty(post.dateRange)  or _StrIsEmpty(post.amountRange)  or
     _StrIsEmpty(post.entryMode)  or _StrIsEmpty(post.description)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(TransactionHistoryClient, 'transaction-history', 9090)

 local result = client:getTransactionLog(post.cardNumber, post.numOfResults, post.dateRange, post.amountRange, post.entryMode, post.description)
 GenericObjectPool:returnConnection(client)

 ngx.say(table.concat(result, ","))

end

return _M
