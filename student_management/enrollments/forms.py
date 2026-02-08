from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control',
            }),
            'course': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
