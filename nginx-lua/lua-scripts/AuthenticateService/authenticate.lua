local _M = {}

local function _StrIsEmpty(s)
 return s == nil or s == ''
end

function _M.authenticate()
 local GenericObjectPool = require 'GenericObjectPool'
 local AuthenticateServiceClient = require 'bank_AuthenticateService'
 local ngx = ngx

 ngx.req.read_body()
 local post = ngx.req.get_post_args()

 if (_StrIsEmpty(post.username) or _StrIsEmpty(post.password)) then
   ngx.status = ngx.HTTP_BAD_REQUEST
   ngx.say(post.username)
   ngx.say(post.password)
   ngx.say("Incomplete arguments")
   ngx.log(ngx.ERR, "Incomplete arguments")
   ngx.exit(ngx.HTTP_BAD_REQUEST)
 end

 local client = GenericObjectPool:connection(AuthenticateServiceClient, 'authenticate-service', 9090)

 local result = client:authenticate(post.username, post.password)
 GenericObjectPool:returnConnection(client)

 ngx.say(result)

end

return _M
