from django.contrib import admin
from .models import vlog, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display=['id', 'title']
    list_display_links=['id', 'title']


class VlogAdmin(admin.ModelAdmin):

    list_display=['id', 'title', 'created', 'updated']
    list_display_links=['id', 'title']
    list_filter=['id', 'created', 'updated']

admin.site.register(vlog, VlogAdmin)
