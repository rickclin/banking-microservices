local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.searchTransactions()
 local GenericObjectPool = require 'GenericObjectPool'
 local CardManagementClient = require 'bank_CardManagement'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.cardNumber) or _StrIsEmpty(post.description)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(CardManagementClient, 'card-management', 9090)

 local result = client:searchTransactions(post.cardNumber, post.description)
 GenericObjectPool:returnConnection(client)

 ngx.say(table.concat(result, ","))

end

return _M
