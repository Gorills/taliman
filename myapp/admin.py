from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Breadcrumbs, Config, Social, Phone, Meta, Breadcrumbs, Sale
from djsingleton.admin import SingletonAdmin

class SocialAdmin(admin.TabularInline):
    model = Social
    extra = 0
    min_num = 1

class PhonesAdmin(admin.TabularInline):
    model = Phone
    extra = 0
    min_num = 1


class ConfigAdmin(SingletonAdmin):
    list_display = ('name', 'email', 'time', 'logo_img', 'logo_text', 'map')
    fields = ('name', 'email', 'time', 'logo_img', 'logo_text', 'map')
    save_on_top = True

    inlines = [
        PhonesAdmin,
        SocialAdmin,
        
    ]
admin.site.register(Config, ConfigAdmin)

class MetaAdmin(SingletonAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_subtitle', 'meta_keywords', 'domen')
    save_on_top = True


admin.site.register(Meta, MetaAdmin)

admin.site.register(Breadcrumbs, SingletonAdmin)

class SaleForm(forms.ModelForm):
    text = forms.CharField(label='Текст акции', widget=CKEditorUploadingWidget())
    class Meta:
        model = Sale
        fields = '__all__'

class SaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', )
    save_on_top = True
    form = SaleForm
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Sale, SaleAdmin)