from django.contrib import admin

# Register your models here.

from .models import Contact, Review, ContactPopup, ContactFull

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date', 'moderate')
    list_editable = ('moderate', )

@admin.register(ContactPopup)
class ContactPopupAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date', 'message')



@admin.register(ContactFull)
class ContactFullAdmin(admin.ModelAdmin):
    list_display = ('name_2', 'tel_2', 'email_2', 'theme_2', 'date_2', 'message_2')

