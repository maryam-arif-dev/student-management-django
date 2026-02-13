from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Restrict Pages to Logged-in Users
@login_required(login_url='core:login')
# List View 
def course_list(request):
    courses = Course.objects.all().order_by("-created_at")
    paginator = Paginator(courses, 5)  # 5 courses per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj":page_obj,
    }
    return render(request, 'courses/course_list.html', context)
# Add View 
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('courses:list')
        else:
            messages.error(request, 'Failed to add course. Please check the form.')
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})

# Edit an existing course
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('courses:list')
        else:
            messages.error(request, 'Failed to add course. Please check the form.')
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form})

# Delete an course 
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.delete()
        messages.warning(request, 'Course deleted successfully!')
        return redirect('courses:list')

    return render(request, 'courses/delete_course.html', {'course': course})
