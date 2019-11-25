from django.contrib import admin
from tours.models import *


# Register your models here.
from tours.models import Article, ArticleSection


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'start_date')
    date_hierarchy = 'start_date'


@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)



class TourTypeInlineAdmin(admin.TabularInline):
    model = TourType


@admin.register(ToursBanner)
class TourBanerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TourTypeInlineAdmin]


@admin.register(TourSection)
class TourSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ArticleSection)
class ArticleSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)