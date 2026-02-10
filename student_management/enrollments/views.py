from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Enrollment
from .forms import EnrollmentForm
from django.contrib.auth.decorators import login_required

# Restrict Pages to Logged-in Users
@login_required(login_url='core:login')
# List all enrollments
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

# Add a new enrollment
def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment added successfully!')
            return redirect('enrollments:list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollments/add_enrollment.html', {'form': form})

# Edit an existing enrollment
def edit_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment updated successfully!')
            return redirect('enrollments:list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'enrollments/edit_enrollment.html', {'form': form})

# Delete an enrollment
def delete_enrollment(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)
    if request.method == 'POST':
        enrollment.delete()
        messages.warning(request, 'Enrollment deleted successfully!')
        return redirect('enrollments:list')
    return render(request, 'enrollments/delete_enrollment.html', {'enrollment': enrollment})
