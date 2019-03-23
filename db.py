import psycopg2
import random
def server_conncetion():
    con = psycopg2.connect(
        host = "localhost",
        database = "fuelfactory",
        user = "postgres",
        password = "1111")
    return con

def add_fuel_id():
    fuel_id = input('Fuel id -> ')
    return fuel_id

def add_fuel_price():
    fuel_price = input('Fuel price -> ')
    return fuel_price

def add_fuel_provider():
    fuel_provider = input("Fuel provider -> ")
    return fuel_provider

def add_fuel_type():
    fuel_type = input('Fuel type -> ')
    return fuel_type

def add_providers_name():
    providers_name = input('Providers name -> ')
    return providers_name

def add_providers_city():
    providers_city = input('Providers city -> ')
    return providers_city

def add_providers_phone_number():
    providers_phone_number = input('Providers phone number -> ')
    return providers_phone_number

def add_providers_id():
    providers_id = input('Providers id -> ')
    return providers_id

def add_sales_fuel():
    sales_fuel = input('Sales fuel -> ')
    return sales_fuel

def add_sales_gas_station():
    sales_gas_station = input('Sales gas station -> ')
    return sales_gas_station

def add_sales_date():
    sales_date = input('Sales date -> ')
    return sales_date

def add_sales_salesman():
    sales_salesman = input('Sales salesman -> ')
    return sales_salesman

def add_sales_liters():
    sales_liters = input('Sales liters -> ')
    return sales_liters

def add_sales_id():
    sales_id = input('Sales id -> ')
    return sales_id



def view_all_db():
    con = server_conncetion()
    cur = con.cursor()
    cur.execute("SELECT id, listed, price, provider, type FROM fuel")
    print('------------------------Fuel--------------------------------------------------------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[id] {r[0]}  [listed]  {r[1]}  [price]  {r[2]}   [provider]  {r[3]}   [type]  {r[4]}")
    cur.execute("SELECT id, name, phone_number, city FROM providers")
    print('----------------------Providers--------------------------------------------------------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[id]  {r[0]}  [name]  {r[1]}  [phone_number]  {r[2]}  [city]  {r[3]}")
    cur.execute("SELECT id, gas_station, date, fuel, salesman, liters FROM sales")
    print('------------------------Sales-------------------------------------------------------------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[id]  {r[0]}  [gas_station]  {r[1]}  [date]  {r[2]}  [type]  {r[3]}  [salesman]  {r[4]}  [liters]  {r[5]}")
    con.commit()
    cur.close()
    con.close()

def create_fuel():
    con = server_conncetion()
    cur = con.cursor()
    price = add_fuel_price()
    provider = add_fuel_provider()
    type = add_fuel_type()
    id = add_fuel_id()
    t = bool(1)
    cur.execute("INSERT INTO fuel (price, provider, type, id, listed) VALUES (%s, %s, %s, %s, %s)", (price, provider, type, id, t))
    con.commit()
    print('Object created in fuel !')

def create_providers():
    con = server_conncetion()
    cur = con.cursor()
    name = add_providers_name()
    city = add_providers_city()
    phone_number = add_providers_phone_number()
    id = add_providers_id()
    cur.execute("INSERT INTO providers (name, city, phone_number, id) VALUES (%s, %s, %s, %s)", (name, city, phone_number, id))
    con.commit()
    print('Object created in providers !')

def create_sales():
    con = server_conncetion()
    cur = con.cursor()
    fuel = add_sales_fuel()
    gas_station = add_sales_gas_station()
    date = add_sales_date()
    salesman = add_sales_salesman()
    liters = add_sales_liters()
    id = add_sales_id()
    cur.execute("INSERT INTO sales (fuel, gas_station, date, salesman, liters, id) VALUES (%s, %s, %s, %s, %s, %s)", (fuel, gas_station, date, salesman, liters, id))
    con.commit()
    print('Object created in sales !')

def edit_db():
    con = server_conncetion()
    cur = con.cursor()
    edit = input('Tell me which table you want edit ')
    if edit == 'fuel':
        column = input('Write your column name')
        id = input('Tell me id of your element to be edited')
        newname = input('Write new name of the element')
        cur.execute(f"UPDATE {edit} SET {column} = '{newname}' where id = '{id}'")
        con.commit()
        print('Object successfully EDITED !')
    elif edit == 'providers':
        column = input('Write your column name')
        id = input('Tell me id of your element to be edited')
        newname = input('Write new name of the element')
        cur.execute(f"UPDATE {edit} SET {column} = '{newname}' where id = '{id}'")
        con.commit()
        print('Object successfully EDITED !')
    elif edit == 'sales':
        column = input('Write your column name')
        id = input('Tell me id of your element to be edited')
        newname = input('Write new name of the element')
        cur.execute(f"UPDATE {edit} SET {column} = '{newname}' where id = '{id}'")
        con.commit()
        print('Object successfully EDITED !')
    else:
        print('Incorrect Table name, only allowed -> fuel, -> providers, -> sales ')

def delete_db():
    con = server_conncetion()
    cur = con.cursor()
    delete = input('Tell me in which table you want to delete ')
    if delete == 'fuel':
        column = input('Write your column name ')
        value = input('> or = or < ')
        info = input('Tell me info ')
        cur.execute(f"DELETE FROM {delete} WHERE {column} {value} '{info}'")
        con.commit()
        print('Object successfully DELETED !')
    elif delete == 'providers':
        column = input('Write your column name')
        value = input('> or = or < ')
        info = input('Tell me info ')
        cur.execute(f"DELETE FROM {delete} WHERE {column} {value} '{info}'")
        con.commit()
        print('Object successfully DELETED !')
    elif delete == 'sales':
        column = input('Write your column name')
        value = input('> or = or < ')
        info = input('Tell me info')
        cur.execute(f"DELETE FROM {delete} WHERE {column} {value} '{info}'")
        con.commit()
        print('Object successfully DELETED !')
    else:
        print('Incorrect Table name, only allowed -> fuel, -> providers, -> sales ')

def random_create():
    con = server_conncetion()
    cur = con.cursor()
    price_arr = ['26.53', '28.99', '30.21', '25.98', '30.44', '27.52', '29.41', '31.19', '29.87']
    type_arr = ['92 EURO', '95 EURO', '98 EURO', 'GAS', '92', '95', '98', 'DIESEL']
    provider_arr = ['TNK', 'Glushko', 'KLO', 'Amic', 'Socar', 'WOG']
    name_arr = ['Dianne Brook', 'Curtis Cook', 'Victor Bishop', 'Pamela Fletcher', 'Matthew Turner', 'Stacey Longman', 'James Allford']
    phone_arr = ['0678941232', '0985763519', '0964592381', '0667435601', '0965210982', '0986743162', '0675326006']
    city_arr = ['Kyiv', 'Moscow', 'Kharkiv', 'Lviv', 'Astana', 'Piter', 'London', 'New-York', 'Donetsk']
    date_arr = ['10.01.2018', '12.02.2019', '17.06.2018', '27.03.2019', '26.04.2019', '02.02.2019', '07.07.2019', '28.12.2018']
    table = input('Tell me in which table you want to add random ')
    if table == 'fuel':
        price = random.choice(price_arr)
        type = random.choice(type_arr)
        provider = random.choice(provider_arr)
        id = input('Tell me id of the element to be added')
        listed = bool(1)
        cur.execute("INSERT INTO fuel (price, type, provider, id, listed) values (%s, %s, %s, %s, %s)", (price, type, provider, id, listed))
        con.commit()
        print('Random object created in sales !')
    elif table == 'providers':
        name = random.choice(provider_arr)
        city = random.choice(city_arr)
        phone_number = random.choice(phone_arr)
        id = input('Tell me id of the element to be added')
        cur.execute("INSERT INTO providers (name, city, phone_number, id) values (%s, %s, %s, %s)", (name, city, phone_number, id))
        con.commit()
        print('Random object created in providers')
    elif table == 'sales':
        fuel = random.choice(type_arr)
        gas_station = random.randint(1, 25)
        date = random.choice(date_arr)
        id = input('Tell me id of the element to be added')
        salesman = random.choice(name_arr)
        liters = random.randint(1, 50)
        cur.execute("INSERT INTO sales (fuel, gas_station, date, id, salesman, liters) values (%s, %s, %s, %s, %s, %s)",
                    (fuel, gas_station, date, id, salesman, liters))
        con.commit()
        print('Random object created in sales')
    else:
        print('Incorrect Table name, only allowed -> fuel, -> providers, -> sales ')

def search_by_date_sales():
    con = server_conncetion()
    cur = con.cursor()
    date1 = input('From date ')
    date2 = input('To date ')
    cur.execute(f"SELECT id, gas_station, date, fuel, salesman, liters FROM sales WHERE DATE(date)  between '{date1}' and '{date2}'")
    rows = cur.fetchall()
    for r in rows:
        print(f"[id] {r[0]}  [gas_station]  {r[1]}  [date]  {r[2]}   [fuel]  {r[3]}  [salesman]  {r[4]} [liters] {[5]}")

def search_by_listed_fuel():
    con = server_conncetion()
    cur = con.cursor()
    value = input('Enter True or False')
    cur.execute(f"SELECT id, listed, price, provider, type FROM fuel WHERE listed = '{value}' ")
    rows = cur.fetchall()
    for r in rows:
        print(f"[id] {r[0]}  [listed]  {r[1]}  [price]  {r[2]}   [provider]  {r[3]}  [type]  {r[4]}")

def search_2_2():
    con = server_conncetion()
    cur = con.cursor()
    date1 = input('From date ')
    date2 = input('To date ')
    value = input('Is it listed? Input True or False')
    cur.execute(f"SELECT fuel.type, sales.salesman, sales.date  FROM fuel "
                f"INNER JOIN sales ON fuel.type = sales.fuel  WHERE sales.date"
                f"  between '{date1}' and '{date2}' AND fuel.listed = {value}")
    rows = cur.fetchall()
    for r in rows:
        print(f"{r[0]} {r[1]} {r[2]}")

def word_search():
    con = server_conncetion()
    cur = con.cursor()
    table = input('Enter table ')
    column = input('Enter column name ')
    phrase = input('Enter phrase you want to find ')
    if table == 'fuel':
        cur.execute(f"SELECT * FROM fuel WHERE {column} LIKE '%{phrase}%'")
        rows = cur.fetchall()
        for r in rows:
            print(f"[id] {r[0]}  [listed]  {r[1]}  [price]  {r[2]}   [provider]  {r[3]}   [type]  {r[4]}")
    if table == 'providers':
        cur.execute(f"SELECT * FROM providers WHERE {column} LIKE '%{phrase}%'")
        rows = cur.fetchall()
        for r in rows:
            print(f"[id]  {r[0]}  [name]  {r[1]}  [phone_number]  {r[2]}  [city]  {r[3]}")
    if table == 'sales':
        cur.execute(f"SELECT id, gas_station, date, fuel, salesman, liters FROM sales WHERE {column} LIKE '%{phrase}%'")
        rows = cur.fetchall()
        for r in rows:
            print(f"[id]  {r[0]}  [gas_station]  {r[1]}  [date]  {r[2]}  [type]  {r[3]}  [salesman]  {r[4]}  [liters]  {r[5]}")
    else:
        print('Incorrect Table name, only allowed -> fuel, -> providers, -> sales ')

