from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Contact, Review, ContactPopup, ContactFull

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

class FullContactsForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactFull
        fields = ['name_2', 'tel_2', 'email_2', 'theme_2', 'message_2', 'captcha']
        widgets = {
            'name_2': forms.TextInput(attrs={'class': 'contacts__input', 'placeholder': 'Имя'}),
            'tel_2': forms.TextInput(attrs={'class': 'contacts__input', 'placeholder': 'Телефон'}),
            'email_2': forms.EmailInput(attrs={'class': 'contacts__input', 'placeholder': 'Email'}),
            'theme_2': forms.TextInput(attrs={'class': 'contacts__input', 'placeholder': 'Тема сообщения'}),
            'message_2': forms.Textarea(attrs={'class': 'contacts__textarea', 'placeholder': 'Сообщение'}),
        }
        labels = {
            'name_2': '',
            'tel_2': '',
            'email_2': '',
            'theme_2': '',
            'message_2': '',
        }


class RestContactsForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactPopup
        fields = ['name', 'tel', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'popup__input', 'placeholder': 'Имя'}),
            'tel': forms.TextInput(attrs={'class': 'popup__input', 'placeholder': 'Телефон'}),

            'message': forms.Textarea(attrs={'class': 'popup__input', 'placeholder': 'Сообщение'}),
        }
        labels = {
            'name': '',
            'tel': '',

            'message': '',
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