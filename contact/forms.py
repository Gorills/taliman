from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Contact, Review

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'tel', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'about-contacts__input', 'placeholder': 'Имя'}),
            'tel': forms.TextInput(attrs={'class': 'about-contacts__input', 'placeholder': 'Телефон'}),
            
        }
        labels = {
            'name': '',
            'tel': '',
            

        }

class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Review
        fields = ['name', 'tel', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'review__input', 'placeholder': 'Имя'}),
            'tel': forms.TextInput(attrs={'class': 'review__input', 'placeholder': 'Телефон'}),
            'message': forms.Textarea(attrs={'class': 'review__input', 'placeholder': 'Отзыв'}),
            
        }
        labels = {
            'name': '',
            'tel': '',
            'message': '',
            

        }