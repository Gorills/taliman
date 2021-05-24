from django.utils.deprecation import MiddlewareMixin
from .models import Serv, Portfolio




class GetServ(MiddlewareMixin):
    def process_request(self, request):

        serv_list= Serv.objects.all().order_by('id')
       
        request.serv_list = serv_list
        
        print(request.serv_list)
        return None


class GetPortfolio(MiddlewareMixin):
    def process_request(self, request):

        portfolio_list= Portfolio.objects.all().order_by('-id')[:6]
       
        request.portfolio_list = portfolio_list
        
        print(request.portfolio_list)
        return None