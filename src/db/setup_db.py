from typing import final
import pymysql
import os, sys
from dotenv import load_dotenv
print(os.curdir)
from helper_modules.input_helper import input_helper

class DBInitializer:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    
    def set_up_db_connection(self):
        self.con = pymysql.connect(
            self.host,
            self.user,
            self.password,
            self.db
        )
        self.cur = self.con.cursor()
    
    def disconnect_database(self):
        self.con.close()

def setup_db_connection():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get('mysql_pass')
    database = os.environ.get("mysql_db")
    try:
        connection = pymysql.connect(
            host,
            user,
            password,
            database
        )
        return connection
    except:
        print('Cannot load database, check your setup')


def show_db_data(selection, connection_t='real'):
    
    try:
        if connection_t == 'real':
            connection = setup_db_connection()
            cursor = connection.cursor()
            print('In real')
        else:
            connection = connection_t
            cursor = connection.cursor()
            

        cursor.execute(f'SELECT * FROM {selection}')
        rows = cursor.fetchall()
        print('inside the func', rows)
        #get the table names
        column_names = get_column_names(cursor, selection)

        for row in rows:
            print(f'{column_names[0]}: {row[0]}, {column_names[1]}: {row[1]}, {column_names[2]}: {row[2]}')

    except Exception as error:
        print('Cannot load database, check your setup', error)
    else:
        if connection.open:
            connection.commit()
            cursor.close()
            connection.close()

        return rows

    return []

def get_column_names(cursor, selection):
    cursor.execute(f'SHOW COLUMNS FROM {selection}')
    column_names = cursor.fetchall()
    
    list_name = [name[0] for name in column_names]
    return list_name

def add_to_db(selection, new_value_one, new_value_two):
    connection = setup_db_connection()
    cursor = connection.cursor()
    column_names = get_column_names(cursor, selection)
    print('I can reach here')
    print(selection, column_names, new_value_one, new_value_two)
    try:
        cursor.execute(
            f'INSERT INTO {selection} ( {column_names[1]},{column_names[2]} )'
            + f'VALUES ( "{new_value_one}",{new_value_two} );'
        )
    except Exception as error:
        print(error)

    connection.commit()
    cursor.close()
    connection.close()

def update_to_db(selection):
    connection = setup_db_connection()
    cursor = connection.cursor()
    column_names = get_column_names(cursor, selection)[1:]

    promt_msg = "Please insert one of the index from above to update: "
    previous_input_index = input_helper(promt_msg, [], True, False)

    for col_name in column_names:
        new_input = input(f'New value for {col_name}: ')
        if new_input == "":
            continue
        else:
            cursor.execute(f'UPDATE {selection} SET {col_name} = {new_input}'
                        + f' WHERE id = {previous_input_index}')
            print('Data has been updated!')
            print('\n')

    connection.commit()
    cursor.close()
    connection.close()

def delete_to_db(selection, index):
    connection = setup_db_connection()
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM {selection} WHERE id = {index};')
    print(f'Index entry: {index} has now been deleted!')
    print('\n')

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    show_db_data('product', setup_db_connection)
# cursor = connection.cursor()
# cursor.execute('CREATE DATABASE mini_project_storage')
# cursor.execute('CREATE TABLE product (id INT NOT NULL AUTO INCREMENT)')