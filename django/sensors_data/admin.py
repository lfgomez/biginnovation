from django.contrib import admin

from .models import SensorType, Unit, Measure, DataType, Data

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1

class SensorTypeAdmin(admin.ModelAdmin):
    inlines = [UnitInline,]

class DataInline(admin.TabularInline):
    model = Data
    extra = 1

class MeasureAdmin(admin.ModelAdmin):
    ordering = ['unixtime',]
    inlines = [DataInline,]

admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(Unit)
admin.site.register(DataType)
admin.site.register(Measure, MeasureAdmin)
