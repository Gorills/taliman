from django.shortcuts import render
from .models import Serv, ServChildren, ServImage
# Create your views here.
def serv(request):

    context = {
        'servs': Serv.objects.all()

    }

    return render(request, 'serv/index.html', context)



def serv_detail(request, slug):
    
    context = {
        'serv': Serv.objects.get(slug=slug),
    }
    return render(request, "serv/serv_detail.html", context)


def servchildren_detail(request, slug, parent):
    servise = ServChildren.objects.get(slug=slug)
    
    context = {
        'children': servise,
    }
    return render(request, "serv/servchildren_detail.html", context)