from django.contrib import admin
from contacts.models import *


class ContactOfficeInlineAdmin(admin.TabularInline):
    model = OfficeContact


class ScheduleItemInlineAdmin(admin.TabularInline):
    model = ScheduleItem


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ContactOfficeInlineAdmin, ScheduleItemInlineAdmin]


class UnitContactInlineAdmin(admin.TabularInline):
    model = UnitContact


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [UnitContactInlineAdmin]
