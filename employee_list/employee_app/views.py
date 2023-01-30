from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import *
from .forms import *


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_app/employee_list.html', context)


class NewEmployee(TemplateView):
    template_name = 'employee_app/new_employee.html'

    def get(self, request, *args, **kwargs):
        form = EmployeeForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                position_name = form.cleaned_data['position_name']
                email = form.cleaned_data['email']
                location = form.cleaned_data['location']
                photo = form.cleaned_data['photo']
                birthday = form.cleaned_data['birthday']
                phone = form.cleaned_data['phone']

                form.save()
                return redirect('/')
            context = {'form': form}
            return render(request, self.template_name, context)


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('/')


def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return redirect('/')


def view_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    context = {'employee': employee}
    return render(request, 'employee_app/view_employee.html', context)




