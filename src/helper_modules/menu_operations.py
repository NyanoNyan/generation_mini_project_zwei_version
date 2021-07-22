from helper_modules.operations_funcs import selection_print, read_data, view_data, confirmation_prints, show_with_index, update_data, delete_data, extra_order_info, append_data, update_dict_data
from helper_modules.file_handler import read_data
from helper_modules.orders import read_orders, write_orders, status
from helper_modules.csv_handler import write_csv

def main_menu():

    print('\n')
    print('Press 0 to exit the application and save the data changes')
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

def product_menu(selection, data_storage, filename):
    selection_print(selection)
    while True:
        product_menu_selection = input('Please select an option or press m to see the menu options: ')
        
        if product_menu_selection == "0":
            break
        
        elif product_menu_selection == "1":
            view_data(selection, data_storage)
            
        elif product_menu_selection == "2":
            data_storage.append(append_data(selection, data_storage))
            
        elif product_menu_selection == "3":
            show_with_index(selection, data_storage)
            data_storage = update_dict_data((data_storage))
            
        elif product_menu_selection == "4":
            show_with_index(selection, data_storage)
            delete_input = input(f'Please insert the index of the {selection} you want deleted: ')
            data_storage = delete_data(delete_input, data_storage)
            
        elif product_menu_selection == "m":
            selection_print(selection)
            
        else:
            print('Please enter a valid input')
        
    return data_storage
    
def courier_menu(selection, data_storage, filename):
    selection_print(selection)
    while True:
        courier_menu_selection = input('Please select an option or press m to see the menu options: ')
        
        if courier_menu_selection == "0":
            break
        
        elif courier_menu_selection == "1":
            view_data(selection, data_storage)
            
        elif courier_menu_selection == "2":
            data_storage.append(append_data(selection, data_storage))
            
        elif courier_menu_selection == "3":
            show_with_index(selection, data_storage)
            data_storage = update_dict_data((data_storage))
            
        elif courier_menu_selection == "4":
            show_with_index(selection, data_storage)
            delete_input = input(f'Please insert the index of the {selection} you want deleted: ')
            data_storage = delete_data(delete_input, data_storage)
            
        elif courier_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')
        
    return data_storage

def orders_menu(selection, data_storage, data_storage_product, data_storage_courier):
    selection_print(selection)
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
            try:
                new_object_data = extra_order_info(data_storage_product, data_storage_courier)
                print('\n')
                data_storage.append(new_object_data)
        
                print('\n')
                print('New order has been added!')
                print('\n')
            except Exception as error:
                print('\n')
                print(error)
                print('Value was not recorded, please try again.')
                print('\n')
                
        elif orders_menu_selection == "3":
            show_with_index(selection, data_storage)
            print('\n')
            try: 
                previous_input_index = int(input(f'Please insert the {selection} status index you want to change: '))
                [print(index, status_name) for index, status_name in enumerate(status)]
                new_status_index = int(input('Please insert the new order status index:'))
                data_storage = update_data(previous_input_index, new_status_index, data_storage, selection)
                
            except Exception as e:
                print('\n')
                print(f'Error: {e}')
                print('Please make sure to enter a valid option')
                print('\n')
                
        elif orders_menu_selection == "4":
            show_with_index(selection, data_storage)
            data_storage = update_dict_data(data_storage)
                
        elif orders_menu_selection == "5":
            show_with_index(selection, data_storage)
            print('\n')
            try:
                index_delete = int(input('Please enter the index of order which you want to delete: '))
                deleted = data_storage.pop(index_delete)
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

    return data_storage