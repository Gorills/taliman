from django.db import models
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm



class ContactView(CreateView):
    models = Contact
    form_class = ContactForm
    success_url = '/'
