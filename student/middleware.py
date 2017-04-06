from django.http import HttpResponseRedirect
from django.contrib.auth import SESSION_KEY

#process_request 在请求到来时调用
#process_view(self,request,fnc,arg,kwarg)在本次要执行view函数前调用
#process_response(self,request,response)在执行完View函数准备将响应发到客户端前被执行
#process_exception(self,request,exception),在view抛异常是调用
class LoginMiddleware():
    def process_request(self,request):
        pass