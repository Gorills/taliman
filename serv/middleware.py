from django.utils.deprecation import MiddlewareMixin
from .models import Serv




class GetServ(MiddlewareMixin):
    def process_request(self, request):

        serv_list= Serv.objects.all()
       
        request.serv_list = serv_list
        
        print(request.serv_list)
        return None