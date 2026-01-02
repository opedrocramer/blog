from django.contrib import admin
from .models import Category, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('id', 'title', 'category__name', 'status')

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
