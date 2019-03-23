import db

def controller():
    option = input('0 to QUIT\n1 to SEE DB\n2 to ADD Fuel\n3 to ADD Providers\n'
                   '4 to ADD Sales\n5 to EDIT DB\n6 to DELETE\n7 to ADD RANDOM\n'
                   '8 to SEARCH by date\n')
    if option == '1':
        db.view_all_db()
    elif option == '2':
        db.create_fuel()
    elif option == '3':
        db.create_providers()
    elif option == '4':
        db.create_sales()
    elif option == '5':
        db.edit_db()
    elif option == '6':
        db.delete_db()
    elif option == '7':
        db.random_create()
    elif option == '8':
        db.search_by_date_sales()
    elif option == '0':
         global a
         a = bool(0)
a = bool(1)
while a:
    controller()