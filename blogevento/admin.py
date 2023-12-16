from django.contrib import admin
from .models import blog_evento

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(blog_evento,BlogAdmin)