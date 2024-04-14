from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_length = models.CharField(max_length=30)
    birth_year = models.IntegerField() 
    salary = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def age(self):
        return 2022 - self.birth_year

# views.py
from django.shortcuts import render
from.models import Employee, Department
from django.db.models import Q

def employee_list(request):
    departments = Department.objects.all()
    employees = Employee.objects.all()
    query = request.GET.get('q')
    if query:
        employees = employees.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(department__name__icontains=query))
    return render(request, 'employee_list.html', {'employees': employees, 'departments': departments})
