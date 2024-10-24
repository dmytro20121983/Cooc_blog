from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.

from . import models

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['NAME', 'category', 'author', 'id']
    inlines = [RecipeInline]

@admin.register(models.Recipe)    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'pre_time', 'cooc_time', 'POST']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
