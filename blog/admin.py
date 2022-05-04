from django.contrib import admin
from .models import blog
# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'publish']
admin.site.register(blog)