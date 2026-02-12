from django.shortcuts import render
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
# Global Search View
def global_search(request):
    query = request.GET.get('q')

    students = []
    courses = []
    enrollments = []

    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(address__icontains=query)
        )
        courses = Course.objects.filter(
            Q(name__icontains=query) | 
            Q(code__icontains=query)
        )
        enrollments = Enrollment.objects.filter(
            Q(course__name__icontains=query) | 
            Q(student__first_name__icontains=query) 
        )
    context = {
        'query': query,
        'students': students,
        'courses': courses,
        'enrollments': enrollments,
    }
    return render(request, 'core/search_results.html', context)