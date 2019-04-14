from django.contrib import admin
from .models import Post, PostImage

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'city')
    list_filter = ('type', 'city')
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sight')