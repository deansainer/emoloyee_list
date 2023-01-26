from django.forms import ModelForm
from employee_app.models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
