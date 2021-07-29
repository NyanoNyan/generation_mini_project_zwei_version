import os
import pymysql
from dotenv import load_dotenv

print(os.curdir)
from helper_modules.input_helper import input_helper

## Set this up to use class for viewing, adding and deleting. One big helper helper.
class HelperDB:
    def __init__(self):
        load_dotenv()
        self.host = os.environ.get("mysql_host")
        self.user = os.environ.get("mysql_user")
        self.password = os.environ.get('mysql_pass')
        self.database = os.environ.get("mysql_db")
    
    def set_up_db_connection(self):
        self.conn = pymysql.connect(
            self.host,
            self.user,
            self.password,
            self.database
        )
        self.cur = self.conn.cursor()
    
    def disconnect_database(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
    
    def fetch_all(self, sql):
        self.set_up_db_connection()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.disconnect_database()
        return data

    def get_column_names(self, selection):
        column_names = self.fetch_all(f'SHOW COLUMNS FROM {selection}')
        list_name = [name[0] for name in column_names]
        return list_name
    
    def execute_operation(self, sql):
        self.set_up_db_connection()
        self.cur.execute(sql)
        self.disconnect_database()


def show_db_data(selection, connection_t='real'):
    try:
        if connection_t == 'real':
            print('In real')
            db = HelperDB()
        else:
            db = connection_t

        rows = db.fetch_all(f'SELECT * FROM {selection}')
        print('inside the func', rows)
        #get the table names
        column_names = db.get_column_names(selection)

        for row in rows:
            print(f'{column_names[0]}: {row[0]}, {column_names[1]}: {row[1]}, {column_names[2]}: {row[2]}')

    except Exception as error:
        print('Cannot load database, check your setup', error)
    else:
        if db.conn.open:
            db.disconnect_database()

        return rows

    return []

def add_to_db(selection, new_value_one, new_value_two):
    try:
        db = HelperDB()
        column_names = db.get_column_names(selection)
        print('I can reach here')
        print(selection, column_names, new_value_one, new_value_two)

        db.execute_operation(
            f'INSERT INTO {selection} ( {column_names[1]},{column_names[2]} )'
            + f'VALUES ( "{new_value_one}",{new_value_two} );'
        )
    except Exception as error:
        print('Cannot add data from the database', error)
    else:
        if db.conn.open:
            db.disconnect_database()

def update_to_db(selection):
    try:
        db = HelperDB()
        column_names = db.get_column_names(selection)[1:]

        promt_msg = "Please insert one of the index from above to update: "
        previous_input_index = input_helper(promt_msg, [], True, False)

        for col_name in column_names:
            new_input = input(f'New value for {col_name}: ')
            if new_input == "":
                continue
            else:
                db.execute_operation(
                    f'UPDATE {selection} SET {col_name} = {new_input}'
                    + f' WHERE id = {previous_input_index}'
                )
                print('Data has been updated!')
                print('\n')
    except Exception as error:
        print('Cannot update to Database', error)
    else:
        if db.conn.open:
            db.disconnect_database()


def delete_to_db(selection, index):
    try:
        db = HelperDB()
        db.execute_operation(f'DELETE FROM {selection} WHERE id = {index};')
        print(f'Index entry: {index} has now been deleted!')
        print('\n')
    except Exception as error:
        print('Cannot delete data from the database', error)
    else:
        if db.conn.open:
            db.disconnect_database()

# if __name__ == '__main__':
#     show_db_data('product', setup_db_connection)
# cursor = connection.cursor()
# cursor.execute('CREATE DATABASE mini_project_storage')
# cursor.execute('CREATE TABLE product (id INT NOT NULL AUTO INCREMENT)')

# def setup_db_connection():
#     load_dotenv()
#     host = os.environ.get("mysql_host")
#     user = os.environ.get("mysql_user")
#     password = os.environ.get('mysql_pass')
#     database = os.environ.get("mysql_db")
#     try:
#         connection = pymysql.connect(
#             host,
#             user,
#             password,
#             database
#         )
#         return connection
#     except:
#         print('Cannot load database, check your setup')