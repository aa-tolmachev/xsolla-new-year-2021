from django.shortcuts import render
from employees.models import employees_db

def index(request):

    prev_employees = ''
    cnt_employees = ''
    new_employees = ''
    employees = ''


    for i in range(len(employees_db)):
        employee_form = (f'<input type="radio" name="employee" required'
                    f' value="{employees_db[i]["name"]}">{employees_db[i]["name"]}')

        employee_link = f'<a href="employees/{i}/">Детали</a>'
        employees += f'{employee_form} | {employee_link} <br>'
    



    if request.method == 'POST':
        cnt_employees = request.POST['cnt_employees']
        



    context = {
        'employees': employees,
        'prev_employees': prev_employees,
        'cnt_employees': cnt_employees,
        'new_employees': new_employees,
    }
    return render(request, 'homepage/index.html', context)
