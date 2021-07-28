import pytest

from db.setup_db import setup_db_connection, show_db_data
from unittest import mock

@pytest.fixture
def setup_database():
    ## Set up
    print("\nSet up")
    connection = setup_db_connection()
    cursor = connection.cursor()
    
    cursor.execute(
        f"TRUNCATE TABLE test_product;"
    )
    
    cursor.execute(
        f"INSERT INTO test_product(name, price) VALUES('KitKat', 1.2), ('Coke Zero', 1.4);"
    )
    yield connection
    # Tear down
    print("\nTear down")
    if connection.open == False:
        connection = setup_db_connection()
        cursor = connection.cursor()
    cursor.execute(
        f"TRUNCATE TABLE test_product;"
    )
    connection.commit()
    cursor.close()
    connection.close()

def test_setup(setup_database):
    ## Intial setup check 
    connection = setup_database
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM test_product')
    actual = cursor.fetchall()
    print(actual)
    expected = ((1, 'KitKat', 1.2), (2, 'Coke Zero', 1.4))
    
    assert expected == actual


def test_show_db_data(setup_database):
    actual = show_db_data('test_product', connection_t = setup_database)
    expected = ((1, 'KitKat', 1.2), (2, 'Coke Zero', 1.4))
    
    assert expected == actual