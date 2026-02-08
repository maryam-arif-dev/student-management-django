from django.contrib import admin
from .models import Enrollment

# Register Enrollment in Admin
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    list_filter = ('course', 'enrollment_date')
