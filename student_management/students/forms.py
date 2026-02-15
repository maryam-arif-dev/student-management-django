from django import forms
from .models import Student
from datetime import date
import re
class StudentForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter address', 'rows': 3})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )
    # Prevent Future Date of Birth
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")
        if dob > date.today():
             raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob
    # Phone number validation
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")

        # Remove spaces
        phone = phone.replace(" ", "")
        
        # Phone number International Format validation
        if not re.fullmatch(r"^\+?\d{10,15}$", phone):
            raise forms.ValidationError(
              "Enter a valid phone number (10–15 digits, optional +)."
         )
        return phone
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']
