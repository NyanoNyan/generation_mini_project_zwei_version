import copy

from helper_modules.orders import status
from db.setup_db import show_db_data, add_to_db, HelperDB
from helper_modules.input_helper import input_helper

def selection_print(selection):
    if selection == "product" or selection == "courier":
        print('\n')
        print(f'######### {selection.capitalize()} Menu #########')
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
        print(f'######### {selection.capitalize()} Menu #########')
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
    print(data_storage)
    if len(data_storage) == 0:
        print('Item Inventory is empty')
    else:
        if selection == 'orders':
            for index, data in enumerate(data_storage):
                print('\n')
                print(f'Order number {index + 1}')
                print(data)
                print(f'Customer Name: {data["customer_name"]}')
                print(f'Customer Adress: {data["customer_address"]}')
                print(f'Customer Phone: {data["customer_phone"]}')
                print(f'Courier: {data["courier"]}')
                print(f'Status: {data["status"]}')
                print(f'Items: {data["items"]}')
        else:
            print('\n')
            print('### Item inventory ###')
            print(f'The {selection}s include: ')
            show_db_data(selection)
            print('\n')

def append_data(selection):
    try:
        if selection == 'product':
            new_input_name = input('Please add in the a new product name: ')
            new_input_price = float(input('Please add in the  product price: '))
            new_data = {'name': new_input_name, 'price': new_input_price}
            add_to_db(selection, [new_input_name, new_input_price])
            
            return new_data
        elif selection == 'courier':
            new_input_name = input('Please add in the a new courier name: ') 
            new_input_number = input('Please add in the new courier phone number: ')
            new_data = {'name': new_input_name, 'phone': new_input_number}
            add_to_db(selection, [new_input_name, new_input_number])
            
            
            return new_data
        elif selection == 'orders':
            db = HelperDB()
            ## Use extra_order_info
            ## Load in that function, by passing it variable names such as product and courier
            input_data = extra_order_info('product','courier')
            print(input_data[:3])
            add_to_db(selection, input_data)

    except:
        print('Input is wrong')
    else:
        print('\nData has been added!')
        
def update_dict_data(data_storage):
        print('\n')
        promt_msg = "Please insert one of the index from above to update: "
        condition_list = list(range(len(data_storage)))
        previous_input_index = input_helper(promt_msg, [], True, False)
        try:
            selected_order = data_storage[previous_input_index]
            new_obj = {}
            for key, value in selected_order.items():
                new_input = input(f'New value for {key}: ')
                
                if new_input == "":
                    new_obj[key] = value
                else:
                    if key == 'courier':
                        new_obj[key] = int(new_input)
                    elif key == 'price':
                        new_obj[key] = float(new_input)
                    elif key == 'items':
                        list_indx_values = new_input.strip().split(',')
                        list_indx_values2 = [int(x) for x in list_indx_values]
                        new_obj[key] = list_indx_values2
                    else:
                        new_obj[key] = new_input
            data_storage[previous_input_index] = new_obj
            print('Order has been updated')
            
            return data_storage

        except Exception as e:
            print('\n')
            print(f'Error: {e}')
            print('Please make sure to enter a valid option')
            print('\n')
            return data_storage
        

def update_data(previous_name_index, new_name, data_storage, selection):
    try:
        if selection == "orders":
            previous_name = copy.deepcopy(data_storage[int(previous_name_index)])
            data_storage[int(previous_name_index)]['status'] = status[new_name]
            print(data_storage)
            print('\n')
            print(f'Status of order {previous_name} has been changed to {data_storage[int(previous_name_index)]}')
        else:
            previous_name = data_storage[int(previous_name_index)]
            data_storage[int(previous_name_index)] = new_name
            print('\n')
            print(f'{selection.capitalize()} {previous_name} has been changed to {new_name}')
    except Exception as e:
        print(e)
        print('\n')
        print('#################')
        print(f'{selection} {new_name} not found')
        print('#################')
    
    return data_storage

def delete_data(index, data_storage):
    """Name of the data is removed from the data list which was loaded previously. Then the new updated list is written to the text file.

    Args:
    name (str): name of the product or courier that is going to be deleted
    filename (str): The name of the text file (product.txt or courier.txt)
    data_storage (list): A list containing the data for product or courier

    """

    try:
        name = copy.deepcopy(data_storage[int(index)])
        data_storage.pop(int(index))
        print('\n')
        print(f'{name} is now deleted')
    except:
        print('\n')
        print('#################')
        print('The value you have entered cannot be deleted.')
        print('#################')
    
    return data_storage

def confirmation_prints(name):
        print('\n')
        print(f'{name} has been added!')
        print('\n')

def show_with_index(selection, data_storage):
    print('\n')
    print(f'{selection.capitalize()} list with index')
    for index, order in enumerate(data_storage):
        print(index, order)

def extra_order_info(load_product, load_courier):
    customer_name = input('Please input the customer name: ')
    customer_address = input('Please input the customer address: ')
    phone_number = input('Please input the phone number:')
    
    # Print products list with its index value
    data_product = show_db_data(load_product)
    data_product_indexes = [data[0] for data in data_product]

    # Get valid comma seperated product id's
    while True:
        product_idx_values = input('Please enter the product index e.g. 1, 2, 5. Seperated with a comma to indcate the product you want to add: ')
        list_indx_values = product_idx_values.strip().split(',')
        list_indx_values2 = [int(x) for x in list_indx_values]
        
        if set(list_indx_values2).issubset(set(data_product_indexes)):
            break 
        else:
            print("Please enter valid Product Id's")
    
    # Print courier list with index value
    data_courier = show_db_data(load_courier)
    check_list = [index[0] for index in data_courier]
    print('check_list:', check_list)
    ## Why is this not working?
    prompt_msg = "Please enter the index of the courier: "
    courier_selection = input_helper(prompt_msg, check_list, True, True, True)
    print('courier selection:', courier_selection)
    status = 1
    
    # Don't think I would need to chaneg the dictionary. Much more cleaner format than list
    # in this scenario for add it to the database
    
    return [customer_name, customer_address, phone_number, courier_selection, status, list_indx_values2]