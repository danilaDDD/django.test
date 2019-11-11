from django.contrib import admin
from contacts.models import *

# Register your models here.
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display=('id','title')
 
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display=('value',)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display=('value',)


