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

    prizes = {1 : 'Сертификат в книжный МиФ',
              2 : 'Фимбо',
              3 : 'Лего бэтмобиль',
              4 : 'Кресло пуф',
              5 : 'Нинтендо свитч',
              6 : 'Укулеле',
              7 : 'Окулус VR',
              8 : 'Рюкзак Пиксель и зарядник',
              9 : 'Сертификат плакат ру',
              10 : 'Белый самокат мини скутер',
              11 : 'Массажный коврик Пранамат',
              12 : 'Минискутер самокат чёрный',
              13 : 'Суперпуф',
              14 : 'Сертификат в Литрес',
              15 : 'Наушники Битс синие',
              16 : 'Наушники Битс серебристые',
              17 : 'Лего МайндСтормс',
              18 : 'Лего космическая система NASA',
              19 : 'Гибкое пианино',
              20 : 'Лего Звёздные войны',
              21 : 'Гироролики Slipper',
              22 : 'Яндекс станция серебристая',
              23 : 'Яндекс станция чёрная',
              24 : 'Робот пылесос',
              25 : 'Капсульная кофе машина черная',
              26 : 'Капсульная кофе машина белая',
              27 : 'Электронная книга черная',
              28 : 'Электронная книга синяя',
              29 : 'Проектор cinemood',
              30 : 'Лего Batwing',
              31 : 'Лего ярость Тирэкса',
              32 : 'Игровая консоль Sony PS',

            }

    if len(prev_employees_arr) > 0:
        prev_winners += f'<p  style="font-size:30px;">'


        for winner in prev_employees_arr:
            prev_w = winner[0]
            win_round = winner[1]
            
            if win_round > last_round:
                last_round = win_round
                prev_winners += f'<br><br><b>Round: {last_round} - {prizes[last_round]}</b><br><br>'
            

            if prev_w != 'test':
                prev_winners += f'{prev_w}<br>'

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

        