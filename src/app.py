import os

from helper_modules.orders import write_orders
from helper_modules.menu_operations import courier_menu, main_menu, product_menu, courier_menu, orders_menu
from helper_modules.csv_handler import read_csv, write_csv

def clear_screen():
    os.system('clear')

def app():
    clear_screen()
    filename_product = 'product.csv'
    filename_courier = 'courier.csv'
    filename_order = 'orders.csv'
    
    data_product = read_csv(filename_product)
    data_courier = read_csv(filename_courier)
    data_order = read_csv(filename_order)
    
    while True:
        # clear_screen()
        main_menu_option, selection = main_menu()
        if main_menu_option == "0":
            print("\n")
            print('Thank you for using this application!')
            print('Product and Courier data have now been updated')
            print("\n")
            write_csv(data_product, filename_product)
            write_csv(data_courier, filename_courier)
            write_csv(data_order, filename_order)
            
            break
        elif main_menu_option == "1":
            clear_screen()
            data_product = product_menu(selection, data_product, filename_product)

        elif main_menu_option == "2":
            clear_screen()

            data_courier = courier_menu(selection, data_courier, filename_courier)
        elif main_menu_option == "3":
            clear_screen()

            data_order = orders_menu(selection, data_order, data_product, data_courier)
        else: 
            print('Please enter a valid option')

app()