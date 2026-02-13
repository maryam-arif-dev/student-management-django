from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

# Restrict Pages to Logged-in Users
@login_required(login_url='core:login')
# Fetch data from student
def student_list(request):
    query = request.GET.get('q')
    # Show all students from databse tabel in UI tabe
    students = Student.objects.all()
    # Search view | Show that based on search input value in student list table
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(address__icontains=query)
        )
    paginator = Paginator(students, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, 'students/student_list.html', context)
# Add new Students
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('students:list')
        else:
            messages.error(request, 'Failed to add student. Please check the form.')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {
        'form': form
    })
# Edit an existing student
def edit_student(request, id):
    student = get_object_or_404(Student, id = id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('students:list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form,
        'student': student
    })
# Delete a student 
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        messages.warning(request, "Student deleted successfully!")
        return redirect("students:list")

    return render(request, "students/delete_student.html", {"student": student})
