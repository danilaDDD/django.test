from django.contrib import admin
from tours.models import Tour,TourType,ToursBaner,TourSection

# Register your models here.
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display=('title',)
    list_filter=('title','start_date')
    date_hierarchy='start_date'    
 
@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(ToursBaner)
class TourBanerAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(TourSection)
class TourSectionAdmin(admin.ModelAdmin):
    list_display=('title',)