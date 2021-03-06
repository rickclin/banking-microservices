local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.getRegisteredProducts()
 local GenericObjectPool = require 'GenericObjectPool'
 local RegisteredProductsClient = require 'bank_RegisteredProducts'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.customerId)) then
   ngx.status = ngx.HTTP_BAD_REQUEST

   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(RegisteredProductsClient, 'registered-products', 9090)

 local result = client:getRegisteredProducts(post.customerId)
 GenericObjectPool:returnConnection(client)
 
 ngx.say(table.concat(result["accounts"], ","))
 ngx.say(table.concat(result["cards"], ","))

end

return _M
