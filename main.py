import db

def controller():
    option = input('0 to QUIT\n'
                   '1 to SEE DB    2 to ADD Fuel   3 to ADD Providers   4 to ADD Sales\n'
                   '5 to EDIT DB   6 to DELETE     7 to ADD RANDOM      8 to SEARCH by date in Sales\n'
                   '9 to SEARCH boolean in Fuel    10 to SEARCH         11 to SEARCH by text\n')
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
    elif option == '9':
        db.search_by_listed_fuel()
    elif option == '10':
        db.search_2_2()
    elif option == '11':
        db.word_search()
    elif option == '0':
         global a
         a = bool(0)
a = bool(1)
while a:
    controller()