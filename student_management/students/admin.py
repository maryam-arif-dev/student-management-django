from django.contrib import admin
from .models import Student

# Register Students model.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'date_of_birth',
        'created_at',
         )
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('created_at',)
    
