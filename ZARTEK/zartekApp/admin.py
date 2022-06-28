from django.contrib import admin
from .models import Posts, PostImage

# Register your models here.
# 
#  
class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Posts
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass