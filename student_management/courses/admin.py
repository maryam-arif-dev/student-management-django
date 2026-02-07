from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','code','description','credits','start_date', 'end_date','created_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
