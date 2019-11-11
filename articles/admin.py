from django.contrib import admin
from articles.models import ArticleSection,Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title',)


@admin.register(ArticleSection)
class ArticleSectionAdmin(admin.ModelAdmin):
    list_display=('title',)
