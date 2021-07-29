import pytest

from db.setup_db import HelperDB, show_db_data
from unittest import mock

@pytest.fixture
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