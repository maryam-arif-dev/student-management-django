from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

# List View 
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
# Add View 
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})

# Edit View 
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form})

# Delete View 
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.delete()
        return redirect('courses:list')

    return render(request, 'courses/delete_course.html', {'course': course})
