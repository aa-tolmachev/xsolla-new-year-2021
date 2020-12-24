from django.shortcuts import render
from .models import employees_db


def employee_detail(request, pk):
    name = employees_db[pk]['name']
    city = employees_db[pk]['city']
    context = {
        'name': name,
        'city': city,
    }
    return render(request, 'employees/employee-detail.html', context)
