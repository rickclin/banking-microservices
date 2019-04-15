local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.getCardNumbers()
 local GenericObjectPool = require 'GenericObjectPool'
 local RegisteredProductsDBClient = require 'bank_RegisteredProductsDB'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.customerId)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(RegisteredProductsDBClient, 'registered-products-db', 9090)

 local result = client:getCardNumbers(post.customerId)
 GenericObjectPool:returnConnection(client)

 ngx.say(table.concat(result, ","))

end

return _M
