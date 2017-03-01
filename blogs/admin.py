from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','text','date_added')

admin.site.register(BlogPost,BlogPostAdmin)
