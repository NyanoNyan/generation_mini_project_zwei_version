from helper_modules.operations_funcs import selection_print, read_data, view_data, confirmation_prints, show_with_index, update_data, delete_data, extra_order_info, append_data, update_dict_data, input_helper
from helper_modules.file_handler import read_data
from helper_modules.orders import read_orders, write_orders, status
from helper_modules.csv_handler import write_csv

def main_menu():

    print('\n')
    print('####### Main Menu ########')
    print('Press 0 to exit the application and save the data changes')
    print('Press 1 to go to product menu')
    print('Press 2 to go to couriers menu')
    print('Press 3 to go to orders menu')
    print('\n')

    prompt = 'Please select an option: '
    first_option = input_helper(prompt, ['0','1', '2', '3'], False, True)

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
            # Get the status Order index
            prompt_msg = f'Please insert the {selection} status index you want to change: '
            condition_list = list(range(len(data_storage)))
            previous_input_index = input_helper(prompt_msg, condition_list, True, True)
            
            [print(index, status_name) for index, status_name in enumerate(status)]
            # Get the Status index
            prompt_msg2 = f'Please insert the {selection} status index you want to change: '
            condition_list2 = list(range(len(status)))
            new_status_index = input_helper(prompt_msg2, condition_list2, True, True)
            
            data_storage = update_data(previous_input_index, new_status_index, data_storage, selection)

        elif orders_menu_selection == "4":
            show_with_index(selection, data_storage)
            data_storage = update_dict_data(data_storage)
                
        elif orders_menu_selection == "5":
            show_with_index(selection, data_storage)
            print('\n')
            prompt_msg3 = "Please enter the index of order which you want to delete: '"
            condition_list3 = list(range(len(data_storage)))
            index_delete = input_helper(prompt_msg3, condition_list3, True, True)
            deleted = data_storage.pop(index_delete)

            print('\n')
            print(f'{deleted} has been deleted')
            print('\n')

        elif orders_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')

    return data_storage