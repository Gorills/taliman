from django.contrib import admin

# Register your models here.

from .models import Contact, Review

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'date', 'moderate')
    list_editable = ('moderate', )