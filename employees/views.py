from django.shortcuts import render
from .models import employees_db
from . import psql_methods


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
    last_round = 0

    prev_employees_arr = psql_methods.prev_employees_per_round()

    if len(prev_employees_arr) > 0:
        prev_winners += f'<p  style="font-size:30px;">'


        for winner in prev_employees_arr:
            prev_w = winner[0]
            win_round = int(winner[1])
            
            if win_round > last_round:
                last_round = win_round
                prev_winners += f'<b>Round {last_round}</b><br><br>'
            

            if prev_w != 'test':
                prev_winners += f'<b>{prev_w}</b><br>'

        prev_winners += f'</p>'





    context = {

        'prev_winners':prev_winners
    }
    return render(request, 'employees/prev_winners.html', context)




def prev_winners_old(request):
    prev_winners = ''

    prev_employees_arr = psql_methods.prev_employees()

    if len(prev_employees_arr) > 0:
        
        prev_winners += f'<p  style="font-size:30px;">'
        for prev_w in prev_employees_arr:
            if prev_w != 'test':
                prev_winners += f'<b>{prev_w}</b><br>'
        prev_winners += f'</p>'

    context = {

        'prev_winners':prev_winners
    }
    return render(request, 'employees/prev_winners.html', context)

        