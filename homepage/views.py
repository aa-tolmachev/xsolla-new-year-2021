from django.shortcuts import render
from employees.models import employees_db
from employees import psql_methods

all_employees_arr = [emp['name'] for emp in employees_db]


def index(request):

    global all_employees_arr


    prev_employees = ''
    cnt_employees = ''
    new_employees = ''
    employees = ''

    bad_context = ''

    '''
    for i in range(len(employees_db)):
        employee_form = (f'<input type="radio" name="employee" required'
                    f' value="{employees_db[i]["name"]}">{employees_db[i]["name"]}')

        employee_link = f'<a href="employees/{i}/">Детали</a>'
        employees += f'{employee_form} | {employee_link} <br>'
    '''


    if request.method == 'POST':
        cnt_employees = request.POST['cnt_employees']
        cnt_employees = int(cnt_employees)

        if cnt_employees > 25:
            bad_context = "Оооооочень много счастливчиков"


        max_round = psql_methods.max_round()
        prev_employees_arr = psql_methods.prev_employees()

        print(max_round , prev_employees_arr)






    context = {
        'employees': employees,
        'prev_employees': prev_employees,
        'cnt_employees': cnt_employees,
        'new_employees': new_employees,
        'bad_context': bad_context,
    }
    return render(request, 'homepage/index.html', context)
