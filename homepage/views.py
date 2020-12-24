from django.shortcuts import render
import random
from employees.models import employees_db
from employees import psql_methods

all_employees_arr = [emp['name'] for emp in employees_db]


def index(request):

    global all_employees_arr


    prev_employees = ''
    cnt_employees = ''
    new_employees = ''
    employees = ''
    winners = ''

    bad_context = ''
    winners = ''
    prev_winners = ''

    prev_employees_arr = psql_methods.prev_employees()

    
    if len(prev_employees_arr) > 0:
        '''
        prev_winners += f'<p>НАШИ СЧАСТЛИВЧИКИ</p>'
        prev_winners += f'<p>'
        for prev_w in prev_employees_arr:
            prev_winners += f'{prev_w}<br>'
        prev_winners += f'</p>'
        '''
        prev_winners = f'<a href="employees/prev_winners/">список всех победителей</a>'
    


    if request.method == 'POST':
        cnt_employees = request.POST['cnt_employees']
        cnt_employees = int(cnt_employees)

        if cnt_employees > 0:

            if cnt_employees > 25:
                bad_context = "Оооооочень много счастливчиков"


            max_round = psql_methods.max_round()
            new_round = max_round
            

            round_employees = list(set(all_employees_arr) - set(prev_employees_arr))

            for i in range(10):
                random.shuffle(round_employees)

            round_winners = round_employees[:cnt_employees]
            insert_status = psql_methods.insert_round_resunt(new_round , round_winners)
            max_round = psql_methods.max_round()
            print('=================ROUND WINNERS',insert_status, round_winners)

            winners += f'<p><b>ПОБЕДИТЕЛИ РАУНДА!!!!</b></p>'
            winners += f'<p  style="font-size:40px;">'
            for winner in round_winners:
                winners += f'<b>{winner}</b><br>'
            winners += f'</p>'






    context = {
        'employees': employees,
        'winners':winners,
        'prev_winners':prev_winners,
        'prev_employees': prev_employees,
        'cnt_employees': cnt_employees,
        'new_employees': new_employees,
        'bad_context': bad_context,
    }
    return render(request, 'homepage/index.html', context)
