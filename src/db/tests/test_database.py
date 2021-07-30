from os import path
import pytest

from db.setup_db import HelperDB, show_db_data, add_to_db, update_to_db, delete_to_db
from unittest.mock import patch
from unittest import mock

@pytest.fixture()
def setup_database():
    ## Set up
    print("\nSet up")
    db = HelperDB()
    db.set_up_db_connection()

    db.cur.execute(
        f"TRUNCATE TABLE test_product;"
    )
    
    db.cur.execute(
        f"INSERT INTO test_product(name, price) VALUES('KitKat', 1.2), ('Coke Zero', 1.4);"
    )
    db.disconnect_database()
    
    yield 
    # Tear down
    print("\nTear down")
    if db.conn.open == False:
        db.set_up_db_connection()
        
    db.cur.execute(
        f"TRUNCATE TABLE test_product;"
    )
    db.disconnect_database()

def test_setup(setup_database):
    ## Intial setup check 
    setup_database

    db = HelperDB()
    actual = db.fetch_all('SELECT * FROM test_product')
    print(actual)
    expected = ((1, 'KitKat', 1.2), (2, 'Coke Zero', 1.4))
    
    assert expected == actual


def test_show_db_data(setup_database):
    setup_database
    actual = show_db_data('test_product')
    expected = ((1, 'KitKat', 1.2), (2, 'Coke Zero', 1.4))
    
    assert expected == actual

def test_add_to_db(setup_database):
    setup_database
    add_to_db('test_product', 'Tomato', 1.2)
    db = HelperDB()
    actual = db.fetch_all(f"SELECT * FROM test_product WHERE name = 'Tomato'")[0]
    
    assert 'Tomato' and 1.2 in actual

@patch("builtins.input", side_effect=['2', 'Pepsi', ''])
@patch("builtins.print")
def test_update_to_db(mock_print, mock_input, setup_database):
    setup_database
    mock_input
    update_to_db('test_product')
    
    ## Check if data has gone through database execution
    mock_print.assert_called_with("\nData has been updated!\n")
    assert mock_input.call_count == 3
    
    ## Check if the data has been changed
    db = HelperDB()
    actual = db.fetch_all(f'SELECT * FROM test_product WHERE name = "Pepsi"')[0]
    assert 'Pepsi' in actual

@patch("builtins.print")
def test_delete_to_db(mock_print, setup_database):
    setup_database
    
    # Correct selection leading to deletion
    delete_to_db('test_product', 2)
    mock_print.assert_called_with('Index entry: 2 has now been deleted!\n')
    
    # Wrong selection
    delete_to_db('sfsafaf', 2)
    mock_print.assert_called_with("Cannot delete data from the database. Table 'mini_project_storage.sfsafaf' doesn't exist")