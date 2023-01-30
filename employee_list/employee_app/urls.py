from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('new_employee/', views.NewEmployee.as_view(), name='new_employee'),
    path('delete_employee/<str:employee_id>/', views.delete_employee, name='delete_employee'),
]
