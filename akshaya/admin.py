from django.contrib.gis import admin

# Register your models here.
from .models import CustomUser, Akshaya, Service

# @admin.register(models.MyModel)
@admin.register(Akshaya)
class MyAdmin(admin.OSMGeoAdmin):
    pass

admin.site.register(CustomUser)
admin.site.register(Service)