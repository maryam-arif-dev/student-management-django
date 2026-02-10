from django.shortcuts import render
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment
from django.contrib.auth.decorators import login_required
# Restrict Pages to Logged-in Users
@login_required
# Dashboard View
def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)
