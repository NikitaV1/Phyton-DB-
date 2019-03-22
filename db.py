import psycopg2

def server_conncetion():
    con = psycopg2.connect(
        host = "localhost",
        database = "fuelfactory",
        user = "postgres",
        password = "1111")
    return con

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

def controller():
    con = server_conncetion()
    cur = con.cursor()
    option = input('Print 1 to see DB')
    if option == '1':
        view_all_db()
    elif option == '2':
        create_fuel()
    elif option == '3':
        create_providers()
    elif option == '4':
        create_sales()
    else:
        cur.close()
        con.close()
def view_all_db():
    con = server_conncetion()
    cur = con.cursor()
    cur.execute("SELECT price, provider, type FROM fuel")
    print('----------------------Fuel----------------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[price]  {r[0]}   [provider]  {r[1]}   [type]  {r[2]}")
    cur.execute("SELECT name, city, phone_number, id FROM providers")
    print('---------------Providers---------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[name]  {r[0]}  [city]  {r[1]}  [phone_number]  {r[2]}  [id]  {r[3]}")
    cur.execute("SELECT fuel, gas_station, date, liters, salesman FROM sales")
    print('-----------------Sales----------------')
    rows = cur.fetchall()
    for r in rows:
        print(f"[fuel]  {r[0]}  [gas_station]  {r[1]}  [date]  {r[2]}  [liters]  {r[3]}  [salesman]  {r[4]}")
    con.commit()
    cur.close()
    con.close()

def create_fuel():
    con = server_conncetion()
    cur = con.cursor()
    price = add_fuel_price()
    provider = add_fuel_provider()
    type = add_fuel_type()
    cur.execute("INSERT INTO fuel (price, provider, type) VALUES (%s, %s, %s)", (price, provider, type))
    con.commit()

def create_providers():
    con = server_conncetion()
    cur = con.cursor()
    name = add_providers_name()
    city = add_providers_city()
    phone_number = add_providers_phone_number()
    id = add_providers_id()
    cur.execute("INSERT INTO providers (name, city, phone_number, id) VALUES (%s, %s, %s, %s)", (name, city, phone_number, id))
    con.commit()

def create_sales():
    con = server_conncetion()
    cur = con.cursor()
    fuel = add_sales_fuel()
    gas_station = add_sales_gas_station()
    date = add_sales_date()
    salesman = add_sales_salesman()
    liters = add_sales_liters()
    cur.execute("INSERT INTO sales (fuel, gas_station, date, salesman, liters) VALUES (%s, %s, %s, %s, %s)", (fuel, gas_station, date, salesman, liters))
    con.commit()


while 1:
    controller()