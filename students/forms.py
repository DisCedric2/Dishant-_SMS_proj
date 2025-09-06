from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'course']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None or age < 0:
            raise forms.ValidationError("Please enter a valid age.")
        return age
