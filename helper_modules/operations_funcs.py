import copy

from helper_modules.file_handler import read_data, new_write
from helper_modules.orders import read_orders, write_orders, status

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
            print(f'Status of order {previous_name} has been changed to {data_storage[int(previous_name_index)]}')
        else:
            previous_name = data_storage[int(previous_name_index)]
            data_storage[int(previous_name_index)] = new_name
            new_write(data_storage, filename)
            print('\n')
            print(f'{selection.capitalize()} {previous_name} has been changed to {new_name}')
    except Exception as e:
        print(e)
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
    check_list = [str(number) for number in range(len(load_courier))]
    while True:
        courier_selection = input('Please enter the index of the courier: ')
        
        if courier_selection in check_list:
            break
        else: 
            print('Please enter a valid input')
    status = 'PREPARING'

    new_object_data = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": phone_number,
        "courier": load_courier[int(courier_selection)],
        "status": status
    }

    return new_object_data