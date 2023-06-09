from django.contrib import admin
from .models import *



class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ('id','title','timeCreated','price','cat')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_editable = ('cat',)
    list_filter = ('price', 'timeCreated')
    prepopulated_fields = {'slug': ('title',)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Advertisment, AdvertismentAdmin)
admin.site.register(Category, CategoryAdmin)
