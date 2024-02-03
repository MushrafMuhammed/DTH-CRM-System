from django.contrib import admin
from .models import Administrator, Lead, Status, Telecaller
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Administrator)
admin.site.register(Telecaller)
admin.site.register(Lead, ImportExportModelAdmin)
admin.site.register(Status)


