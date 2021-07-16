from helper_modules.menu_operations import courier_menu, main_menu, product_menu, courier_menu, orders_menu

def app():
    while True:
        main_menu_option, selection = main_menu()
        if main_menu_option == "0":
            print("\n")
            print('Thank you for using this application!')
            print("\n")
            break
        elif main_menu_option == "1":
            product_menu(selection)
        elif main_menu_option == "2":
            courier_menu(selection)
        elif main_menu_option == "3":
            orders_menu(selection)
        else: 
            print('Please enter a valid option')

app()