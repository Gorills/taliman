from django.db import models
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .models import Contact, Review
from .forms import ContactForm, ReviewForm



class ContactView(CreateView):
    models = Contact
    form_class = ContactForm
    success_url = '/contact-us/thank-you/'


def thank(request):
    context = {

    }
    return render(request, 'contact/thank.html', context)


def review(request):
    context = {
        'form': ReviewForm
    }
    return render(request, 'contact/review.html', context)

class ReviewView(CreateView):
    models = Review
    form_class = ReviewForm
    success_url = '/'
    