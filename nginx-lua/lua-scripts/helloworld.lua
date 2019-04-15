local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.getHelloworld()
 local GenericObjectPool = require 'GenericObjectPool'
 local HelloworldServiceClient = require 'helloworld_HelloworldService'
 local ngx = ngx

 --ngx.req.read_body()
 --local post = ngx.req.get_post_args()

 --if (_StrIsEmpty(post.first_name) or _StrIsEmpty(post.last_name) or
 --    _StrIsEmpty(post.username) or _StrIsEmpty(post.password)) then
 --  ngx.status = ngx.HTTP_BAD_REQUEST
 --  ngx.say("Incomplete arguments")
 --  ngx.log(ngx.ERR, "Incomplete arguments")
 --  ngx.exit(ngx.HTTP_BAD_REQUEST)
 --end

 local client = GenericObjectPool:connection(HelloworldServiceClient, 'helloworld-service', 9090)

 local result = client:getHelloworld()
 GenericObjectPool:returnConnection(client)

 ngx.say(result)

end

return _M
