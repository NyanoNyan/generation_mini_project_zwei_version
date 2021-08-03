from os import path, terminal_size
import pytest

from db.setup_db import HelperDB, show_db_data, add_to_db, update_to_db, delete_to_db
from unittest.mock import patch
from unittest import mock

@pytest.fixture()
def setup_database():
    ## Set up
    print("\nSet up")
    db = HelperDB(test=True)
    db.set_up_db_connection()
    print('before the great battle')
    # Removing all data in the beginning
    db.cur.execute("TRUNCATE TABLE test_product;")
    print('I can run this')

    # Adding data
    db.cur.execute(
        f"INSERT INTO test_product(name, price) VALUES('KitKat', 1.2), ('Coke Zero', 1.4);"
    )
    
    db.disconnect_database()
    
    yield 
    # Tear down
    print("\nTear down")
    if db.conn.open == False:
        db.set_up_db_connection()

    db.cur.execute("TRUNCATE TABLE test_product;")
    db.disconnect_database()

def test_setup(setup_database):
    ## Intial setup check 
    setup_database

    db = HelperDB(test=True)
    actual = db.fetch_all('SELECT * FROM test_product')
    print(actual)
    expected = ((1, 'KitKat', 1.2), (2, 'Coke Zero', 1.4))
    
    assert expected == actual


def test_show_db_data():
    actual = show_db_data('status')
    expected = [{'id': 1, 'status': 'preparing'}, {'id': 2, 'status': 'out-for-delivery'}, {'id': 3, 'status': 'delivered'}]
    
    assert expected == actual

def test_add_to_db():
    ### Test adding to product
    add_to_db('product', ['Tomato', 1.2], test=True)
    db = HelperDB(test=True)
    actual = db.fetch_all(f"SELECT * FROM product WHERE name = 'Tomato'", dict_cur=True)
    print(actual)
    assert ('Tomato' and 1.2 in actual[0].values())

    #Reset changes
    db.execute_operation('DELETE FROM product WHERE name = "Tomato"')

    ### Test adding to courier
    add_to_db('courier', ['DPD', '07888665654'], test=True)
    db = HelperDB(test=True)
    actual = db.fetch_all(f"SELECT * FROM courier WHERE name = 'DPD'", dict_cur=True)
    print(actual)
    assert ('DPD' and '07888665654' in actual[0].values())
    
    # Reset changes
    db.execute_operation('DELETE FROM courier WHERE name = "DPD"')

    ### Test adding to orders
    add_to_db('orders', ['Miles', '99th Street', '07872817281',1, 1, [1,2]], test=True)
    db = HelperDB(test=True)

    actual = db.fetch_all(f"SELECT * FROM orders" 
        + " INNER JOIN customer_detail"
        + " ON orders.customer_detail_id = customer_detail_id"
        + " WHERE customer_name = 'Miles';", dict_cur=True)
    print(actual)
    assert ('Miles' and '99th Street' in actual[0].values())
    # Reset changes
    db.execute_operation('TRUNCATE TABLE orders;')
    db.execute_operation('DELETE FROM customer_detail WHERE customer_name = "Miles"')



# @patch("builtins.print")
# def test_delete_to_db(mock_print, setup_database):
#     setup_database
    
#     # Correct selection leading to deletion
#     delete_to_db('test_product', 2)
#     mock_print.assert_called_with('Index entry: 2 has now been deleted!\n')
    
#     # Wrong selection
#     delete_to_db('sfsafaf', 2)
#     mock_print.assert_called_with("Cannot delete data from the database. Table 'mini_project_storage.sfsafaf' doesn't exist")