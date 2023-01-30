from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('new_employee/', views.NewEmployee.as_view(), name='new_employee'),
    path('view_employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('view_employee/<int:employee_id>/', views.view_employee, name='view_employee'),
]
