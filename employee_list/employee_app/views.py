from django.shortcuts import render
from .models import *


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_app/employee_list.html', context)


