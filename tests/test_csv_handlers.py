import pytest
from unittest.mock import patch

from src.helper_modules.csv_handler import read_csv, write_csv, convert_to_correct_type

@pytest.fixture()
def load_fake_data():
    #Load up
    data = [{'name':'Cola', 'price':'1.2'}]
    write_csv(data, 'fake_data.csv')
    data_read = read_csv('fake_data.csv')
    yield data_read
    #Tear down
    write_csv(data, 'fake_data.csv')

def test_convert_to_correct_type():
    # Setup 1 product
    data_product = [{'name': 'KitKat', 'price': '1.2'},
        {'name': 'Coke Zero', 'price': '1.4'}]
    filename_product = 'product'
    expected_product = [{'name': 'KitKat', 'price': 1.2},
                {'name': 'Coke Zero', 'price': 1.4}]
    # Setup 2 orders
    data_orders = [
        {
            'customer_name': 'B',
            'customer_address': '22th Street',
            'customer_phone': '075343434',
            'courier': '2',
            'status': "preparing",
            'items': '[0,1]'
        }
    ]
    filename_orders = 'orders'
    expected_orders = [
        {
            'customer_name': 'B',
            'customer_address': '22th Street',
            'customer_phone': '075343434',
            'courier': 2,
            'status': "preparing",
            'items': [0,1]
        }
    ]
    
    # Setup 3 wrong filename
    filename_product_invalid = 'gg'
    expected_product_invalid = data_product
    
    # Set up 4 wrong data_storage
    data_product_wrong = {'time': {'name': 'KitKat', 'price': '1.2'}, 'same': {'name': 'Coke Zero', 'price': '1.4'}}
    
    # Check if it's working normally
    #Setup 1
    assert convert_to_correct_type(data_product, filename_product) == expected_product
    #Setup 2
    assert convert_to_correct_type(data_orders, filename_orders) == expected_orders
    
    # Wrong input checks
    #Setup 3
    assert convert_to_correct_type(data_product, filename_product_invalid) == expected_product_invalid
    #Setup 4
    assert str(convert_to_correct_type(data_product_wrong, filename_product)) == "'str' object has no attribute 'items'"

## How to convert some data to integers ?
def test_read_csv(load_fake_data):
    ### convert to type doesn't work for test data
    # Setup 1
    expected = load_fake_data
    result = read_csv('fake_data.csv')
    # Setup 2
    result2= read_csv('sfasf.csv')
    expected2 = []
    # Check if it loads with the right filename
    assert expected == result
    # Check if it gives an error if the filename is wrong
    assert expected2 == result2


## Need to make a test file which checks the structure of the data
# then only runs it if it's the correct format
# List and inside the list, dictionary values

## Need to write the tests again. I'm returning, but not displaying the data to the user.
## All returns and no prints. How to solve this?

# How to best use assert?
# How to best to unit testing, using returns to check in actual code?
# Video
# print with return combo?

def test_write_csv(load_fake_data):
    # Correct format
    data = load_fake_data
    filename = 'fake_data.csv'
    write_csv(data, filename)
    result = read_csv(filename)
    
    # Wrong format
    data_wrong = {'time':{'name': 'Nyano', 'price': '0.3'},
        'sime': {'name': 'LL', 'price': '0.4'}
    }
    result_second = write_csv(data_wrong, filename)
    expected = 'The data is not formated correctly'
    
    # List, list format
    list_list_data = [ ['name', 'Nyano', 'price', '0.3'],['name', 'LL', 'price', '0.4'] ]
    result_third = write_csv(list_list_data, filename)
    
    # Correct format
    assert data == result

    # Wrong format
    assert result_second == expected
    
    # List, list format
    assert result_third == expected


# def test_write_orders_csv():
#     data = [
#         {
#             'customer_name': 'B',
#             'customer_address': '22th Street',
#             'customer_phone': '075343434',
#             'courier': 2,
#             'status': "preparing",
#             'items': [0,1]
#         }
#     ]
    
#     write_csv(data, 'orders.csv')