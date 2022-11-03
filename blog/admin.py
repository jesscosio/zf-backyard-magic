from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
from .models import Image

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug',)
    list_display = ('id','title','category','date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25
    summernote_fields = ('content')

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]


admin.site.register(Image, ImageAdmin)
admin.site.register(BlogPost, BlogPostAdmin)