from django.shortcuts import render
from serv.models import Slider, Portfolio
from django.views.generic import ListView, DetailView
from contact.models import Review
from .models import Sale


# Create your views here.
def index(request):

    context = {
        'slides': Slider.objects.all(),
        'portfolios': Portfolio.objects.all(),

    }

    return render(request, 'myapp/index.html', context)


def contacts(request):

    context = {

    }

    return render(request, 'myapp/contacts.html', context)

class PortfolioList(ListView):
    paginate_by = 9
    model = Portfolio
    template_name = 'myapp/portfolio.html'



class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = 'myapp/portfolio_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context


def about(request):

    context = {
        'review': Review.objects.all(),
    }

    return render(request, 'myapp/about.html', context)

class SaleList(ListView):
    model = Sale
    template_name = 'myapp/sale_list.html'
    ordering = 'date'


class SaleDetail(DetailView):
    model = Sale
    