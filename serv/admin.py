from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Serv, ServImage, ServChildren, Slider, Portfolio, PortfolioProperty, PortfolioImage

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent')

admin.site.register(Slider, SliderAdmin)



class ServImageAdmin(admin.TabularInline):
    model = ServImage
    extra = 0
    min_num = 0


class ServChildrenForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = ServChildren
        fields = '__all__'


class ServChildrenAdmin(admin.StackedInline):
    model = ServChildren
    form = ServChildrenForm
    prepopulated_fields = {'slug': ('title',)}
    extra = 0
    min_num = 0

class ServChildrenAdminReg(admin.ModelAdmin):
    model = ServChildren
    form = ServChildrenForm
    list_display = ('title', 'parent', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ServChildren, ServChildrenAdminReg)


class ServAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Serv
        fields = '__all__'


class ServAdmin(admin.ModelAdmin):
    form = ServAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'image_prew', 'description', 'slug')
    
    save_on_top = True

    inlines = [
        ServImageAdmin,
        ServChildrenAdmin,
        
    ]
admin.site.register(Serv, ServAdmin)


# Portfolio
class PortfolioPropertyAdmin(admin.TabularInline):
    model = PortfolioProperty
    extra = 0
    min_num = 0


class PortfolioImageAdmin(admin.TabularInline):
    model = PortfolioImage
    extra = 0
    min_num = 0

class PortfolioForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Portfolio
        fields = '__all__'


class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioForm
    list_display = ('title', 'price', 'adress', 'date')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    inlines = [
        PortfolioPropertyAdmin,
        PortfolioImageAdmin

    ]

admin.site.register(Portfolio, PortfolioAdmin)
