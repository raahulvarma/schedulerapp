from django.contrib import admin
from .models import Scheduler

# Register your models here.

class SchedulerAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'start_date', 'end_date')

admin.site.register(Scheduler, SchedulerAdmin)