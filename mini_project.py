from helper_modules.orders import write_orders
from helper_modules.menu_operations import courier_menu, main_menu, product_menu, courier_menu, orders_menu
from helper_modules.file_handler import new_write, read_data

def app():
    filename_product = 'product.txt'
    filename_courier = 'courier.txt'
    
    data_product = read_data(filename_product)
    data_courier = read_data(filename_courier)
    while True:
        main_menu_option, selection = main_menu()
        if main_menu_option == "0":
            print("\n")
            print('Thank you for using this application!')
            print('Product and Courier data have now been updated')
            print("\n")
            new_write(data_product, filename_product)
            new_write(data_courier, filename_courier)
            
            break
        elif main_menu_option == "1":
            data_product = product_menu(selection, data_product, filename_product)
        elif main_menu_option == "2":
            data_courier = courier_menu(selection, data_courier, filename_courier)
        elif main_menu_option == "3":
            orders_menu(selection)
        else: 
            print('Please enter a valid option')

app()