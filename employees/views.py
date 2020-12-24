from django.shortcuts import render
from .models import employees_db
import psql_methods


def employee_detail(request, pk):
    name = employees_db[pk]['name']
    city = employees_db[pk]['city']
    context = {
        'name': name,
        'city': city,
    }
    return render(request, 'employees/employee-detail.html', context)



def prev_winners(request):
    prev_winners = ''

    prev_employees_arr = psql_methods.prev_employees()

    if len(prev_employees_arr) > 0:
        
        prev_winners += f'<p>НАШИ СЧАСТЛИВЧИКИ</p>'
        prev_winners += f'<p>'
        for prev_w in prev_employees_arr:
            prev_winners += f'{prev_w}<br>'
        prev_winners += f'</p>'

    context = {

        'prev_winners':prev_winners
    }
    return render(request, 'employees/prev_winners.html', context)

        