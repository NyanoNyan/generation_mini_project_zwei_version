import copy

from helper_modules.file_handler import read_data, append_data, new_write
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

def selection_print(selection):
    if selection == "product" or selection == "courier":
        print('\n')
        print(f'### Welcome to your {selection} storage system ###')
        print('\n')
        print('Press 0 to return to the menu')
        print(f'Press 1 to view the {selection} list')
        print(f'Press 2 to create a new {selection}')
        print(f'Press 3 to update your existing {selection}')
        print(f'Press 4 to delete your {selection}')
        print('\n')
    elif selection == 'orders':
        print('\n')
        print(f'### Welcome to your {selection} storage system ###')
        print('\n')
        print('Press 0 to return to the menu')
        print(f'Press 1 to view the {selection}')
        print(f'Press 2 to create a new {selection}')
        print(f'Press 3 to update your existing {selection} status')
        print(f'Press 4 to update your existing {selection} order')
        print(f'Press 5 to delete your existing {selection}')
        print('\n')

def view_data(selection, data_storage):
    """Shows the user the inventory list of either product or courier

    Args:
    data_storage (list): A list containing the data for product or courier
    selection (str): A string containing either 'product' or 'courier'

    """

    if len(data_storage) == 0:
        print('Item Inventory is empty')
    else:
        if selection == 'orders':
            for data in data_storage:
                print(data)
        else:
            print('\n')
            print('### Item inventory ###')
            print(f'The {selection}s include: {", ".join(data_storage)}')
            print('\n')

def update_data(previous_name_index, new_name, filename, data_storage, selection):
    try:
        if selection == "orders":
            previous_name = copy.deepcopy(data_storage[int(previous_name_index)])
            data_storage[int(previous_name_index)]['status'] = status[new_name]
            print(data_storage)
            write_orders(data_storage, filename)
            print('\n')
            print(f'Status of order {previous_name} has been changed to {data_storage[previous_name_index]}')
        else:
            previous_name = data_storage[int(previous_name_index)]
            data_storage[int(previous_name_index)] = new_name
            new_write(data_storage, filename)
            print('\n')
            print(f'{selection.capitalize()} {previous_name} has been changed to {new_name}')
    except:
        print('\n')
        print('#################')
        print(f'{selection} {new_name} not found')
        print('#################')

def delete_data(index, filename, data_storage):
    """Name of the data is removed from the data list which was loaded previously. Then the new updated list is written to the text file.

    Args:
    name (str): name of the product or courier that is going to be deleted
    filename (str): The name of the text file (product.txt or courier.txt)
    data_storage (list): A list containing the data for product or courier

    """

    try:
        name = copy.deepcopy(data_storage[int(index)])
        data_storage.pop(int(index))
        new_write(data_storage, filename)
        print('\n')
        print(f'{name} is now deleted')
    except:
        print('\n')
        print('#################')
        print('The value you have entered cannot be deleted.')
        print('#################')

def confirmation_prints(name):
        print('\n')
        print(f'{name} has been added!')
        print('\n')

def show_with_index(selection, filename):
    if selection == 'orders':
        order_list = read_orders(filename)
        print(f'{selection} list with index')
        for index, order in enumerate(order_list):
            print(index, order)
    else:
        print(f'{selection} list with index')
        data_list = read_data(filename)
        for index, order in enumerate(data_list):
            print(index, order)

def extra_order_info():
    customer_name = input('Please input the customer name: ')
    customer_address = input('Please input the customer address: ')
    phone_number = input('Please input the phone number:')
    
    filename = 'courier.txt'
    load_courier = read_data('courier.txt')
    print('Courier List')
    show_with_index('courier', filename)
    
    while True:
        courier_selection = int(input('Please enter the index of the courier: '))
        
        if courier_selection in range(len(load_courier)):
            break
        else: 
            print('Please enter a valid input')
    status = 'PREPARING'

    new_object_data = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": phone_number,
        "courier": load_courier[courier_selection],
        "status": status
    }

    return new_object_data

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
            view_data(selection, data_storage)
        elif orders_menu_selection == "2":
            new_object_data = extra_order_info()
            data_storage.append(new_object_data)
            write_orders(data_storage, filename)
            print('\n')
            print('New order has been added!')
            print('\n')
        elif orders_menu_selection == "3":
            show_with_index(selection, filename)
            previous_input_index = int(input(f'Please insert the {selection} status index you want to change: '))
            [print(index, status_name) for index, status_name in enumerate(status)]
            new_status_index = int(input('Please insert the new order status index:'))
            update_data(previous_input_index, new_status_index, filename, data_storage, selection)
        elif orders_menu_selection == "4":
            show_with_index(selection, filename)
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
            update_data(previous_input_index, previous_input_index, filename, data_storage, selection)
        elif orders_menu_selection == "5":
            show_with_index(selection, filename)
            index_delete = int(input('Please enter the index of order which you want to delete: '))
            data_storage.pop(index_delete)
            write_orders(data_storage, filename)
        elif orders_menu_selection == "m":
            selection_print(selection)
        else:
            print('Please enter a valid input')