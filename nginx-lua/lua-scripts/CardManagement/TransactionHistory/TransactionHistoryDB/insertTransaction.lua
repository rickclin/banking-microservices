local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.insertTransaction()
 local GenericObjectPool = require 'GenericObjectPool'
 local TransactionHistoryDBClient = require 'bank_TransactionHistoryDB'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.cardNumber) or _StrIsEmpty(post.amount) or
     _StrIsEmpty(post.entryMode)  or _StrIsEmpty(post.description)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(TransactionHistoryDBClient, 'transaction-history-db', 9090)

 ngx.say(post.amount)
 
 local result = client:insertTransaction(post.cardNumber, post.amount, post.entryMode, post.description)
 GenericObjectPool:returnConnection(client)

 ngx.say(result)

end

return _M
