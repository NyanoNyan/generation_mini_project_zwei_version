from helper_modules.operations_funcs import selection_print, read_data, view_data, confirmation_prints, show_with_index, update_data, delete_data, extra_order_info
from helper_modules.file_handler import read_data, append_data
from helper_modules.orders import read_orders, write_orders, status

def main_menu():

    print('\n')
    print('Press 0 to go to exit the application')
    print('Press 1 to go to product menu')
    print('Press 2 to go to couriers menu')
    print('Press 3 to go to orders menu')
    print('\n')
    
    while True:
        first_option = input('Please select an option: ')
        
        if first_option == "1" or first_option == "2" or first_option == "3" or first_option == "0":
            break
        else: 
            print('Please select a valid option!')
    
    if first_option == "1":
        selection = "product"
    elif first_option == "2":
        selection = "courier"
    elif first_option == "3":
        selection = "orders"
    else:
        selection = "None"
    
    return first_option, selection

def product_menu(selection):
    selection_print(selection)
    filename = 'product.txt'
    while True:
        data_storage = read_data(filename)
        product_menu_selection = input('Please select an option or press m to see the menu options: ')
        
        if product_menu_selection == "0":
            break
        elif product_menu_selection == "1":
            view_data(selection, data_storage)
        elif product_menu_selection == "2":
            new_input = input('Please add in the a new product name: ')    
            append_data(new_input, filename)
            confirmation_prints(new_input)
        elif product_menu_selection == "3":
            show_with_index(selection, filename)
            previous_input_index = input(f'Please insert the {selection} index you want to change: ')
            new_name = input('Please insert the new product name:')
            update_data(previous_input_index, new_name, filename, data_storage, selection)
        elif product_menu_selection == "4":
            show_with_index(selection, filename)
            delete_input = input(f'Please insert the index of the {selection} you want deleted: ')
            delete_data(delete_input, filename, data_storage)
        elif product_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')
            
def courier_menu(selection):
    selection_print(selection)
    filename = 'courier.txt'
    while True:
        data_storage = read_data(filename)
        courier_menu_selection = input('Please select an option or press m to see the menu options: ')
        
        if courier_menu_selection == "0":
            break
        elif courier_menu_selection == "1":
            view_data(selection, data_storage)
        elif courier_menu_selection == "2":
            new_input = input('Please add in the a new courier name: ')    
            append_data(new_input, filename)
            confirmation_prints(new_input)
        elif courier_menu_selection == "3":
            show_with_index(selection, filename)
            previous_input_index = input(f'Please insert the {selection} index you want to change: ')
            new_name = input(f'Please insert the new {selection} name:')
            update_data(previous_input_index, new_name, filename, data_storage, selection)
        elif courier_menu_selection == "4":
            show_with_index(selection, filename)
            delete_input = input(f'Please insert the index of the {selection} you want deleted: ')
            delete_data(delete_input, filename, data_storage)
        elif courier_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')

def orders_menu(selection):
    selection_print(selection)
    filename = 'orders.json'
    data_storage = read_orders(filename)
    while True:
        orders_menu_selection = input('Please select an option or press m to see the menu options: ')
        
        if orders_menu_selection == "0":
            break
        elif orders_menu_selection == "1":
            print('### Orders Inventory ###')
            print('\n')
            view_data(selection, data_storage)
            print('\n')
        elif orders_menu_selection == "2":
            new_object_data = extra_order_info()
            print('\n')
            data_storage.append(new_object_data)
            write_orders(data_storage, filename)
            print('\n')
            print('New order has been added!')
            print('\n')
        elif orders_menu_selection == "3":
            show_with_index(selection, filename)
            print('\n')
            try: 
                previous_input_index = int(input(f'Please insert the {selection} status index you want to change: '))
                [print(index, status_name) for index, status_name in enumerate(status)]
                new_status_index = int(input('Please insert the new order status index:'))
                update_data(previous_input_index, new_status_index, filename, data_storage, selection)
            except Exception as e:
                print('\n')
                print(f'Error: {e}')
                print('Please make sure to enter a valid option')
                print('\n')
        elif orders_menu_selection == "4":
            show_with_index(selection, filename)
            print('\n')
            try:
                previous_input_index = int(input('Please insert the new order status index:'))
                selected_order = data_storage[previous_input_index]
                new_obj = {}
                for key, value in selected_order.items():
                    new_input = input(f'New value for {key}: ')
                    if new_input == "":
                        new_obj[key] = value
                    else:
                        new_obj[key] = new_input
                data_storage[previous_input_index] = new_obj
                write_orders(data_storage, filename)
                print('Order has been updated')
                # update_data(previous_input_index, previous_input_index, filename, data_storage, selection)
            except Exception as e:
                print('\n')
                print(f'Error: {e}')
                print('Please make sure to enter a valid option')
                print('\n')
        elif orders_menu_selection == "5":
            show_with_index(selection, filename)
            print('\n')
            try:
                index_delete = int(input('Please enter the index of order which you want to delete: '))
                deleted = data_storage.pop(index_delete)
                write_orders(data_storage, filename)
                print('\n')
                print(f'{deleted} has been deleted')
                print('\n')
            except Exception as e:
                print('\n')
                print(f'Error: {e}')
                print('Please make sure to enter a valid option')
                print('\n')
        elif orders_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')