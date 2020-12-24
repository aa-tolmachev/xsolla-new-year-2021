from django.shortcuts import render
from employees.models import employees_db
import psycopg2

all_employees_arr = [emp['name'] for emp in employees_db]

#heroku PSQL
def PSQL_heroku_keys():
    dbname = 'dbr3jigs1op5oo'
    port = '5432'
    user = 'muwrkppfuyldmk'
    host = 'ec2-54-227-252-202.compute-1.amazonaws.com'
    password = '4c4eabfcaf92f7289ccfc1a314d04a3c3806db72b1bf12fd5f0f40c410b14355'

    PSQL_heroku_keys = {'dbname' : dbname
                        , 'port' : port
                        , 'user' : user
                        , 'host' : host
                        , 'password' : password
                        }

    return PSQL_heroku_keys


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






    context = {
        'employees': employees,
        'prev_employees': prev_employees,
        'cnt_employees': cnt_employees,
        'new_employees': new_employees,
        'bad_context': bad_context,
    }
    return render(request, 'homepage/index.html', context)
