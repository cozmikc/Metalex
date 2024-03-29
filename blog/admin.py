from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ("body",)

# Register your models here.
admin.site.register(Post, BlogPostAdmin)
admin.site.register(PostComment)