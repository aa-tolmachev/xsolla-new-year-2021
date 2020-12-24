import psycopg2

#heroku PSQL
def PSQL_heroku_keys_dict():
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





#Последний раунд
def max_round():

    try:
        PSQL_heroku_keys = PSQL_heroku_keys_dict()

        #создаем подключение к PSQL
        conn = psycopg2.connect("dbname='%(dbname)s' port='%(port)s' user='%(user)s' host='%(host)s' password='%(password)s'" % PSQL_heroku_keys)

        # создаем запрос
        cur = conn.cursor()
        #проверяем, что пользователя ранее не было
        cur.execute("select case when max(round) is null then 0 else max(round) end as max_round from public.xsolla2021")

        result = {'fetch' : cur.fetchall() , 'desc' : cur.description}

        cur.close()
        conn.close()
        max_round = result['fetch'][0][0]
    except:
        max_round = 100

    return max_round


#Получившие подарок
def prev_employees():

    
    PSQL_heroku_keys = PSQL_heroku_keys_dict()

    #создаем подключение к PSQL
    conn = psycopg2.connect("dbname='%(dbname)s' port='%(port)s' user='%(user)s' host='%(host)s' password='%(password)s'" % PSQL_heroku_keys)

    # создаем запрос
    cur = conn.cursor()
    #проверяем, что пользователя ранее не было
    cur.execute("select distinct(name) from public.xsolla2021")

    result = {'fetch' : cur.fetchall() , 'desc' : cur.description}

    cur.close()
    conn.close()

    prev_employees_arr = [x[0] for x in result['fetch']]


    return prev_employees_arr