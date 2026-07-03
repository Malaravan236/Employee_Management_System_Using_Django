from django import forms
from .models import Employee

class Employee_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Employee_id','Name','Department','Salary','Phone','Email','Address','Joining_date','Status']