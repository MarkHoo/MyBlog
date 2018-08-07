from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 在admin后台注册模型
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

