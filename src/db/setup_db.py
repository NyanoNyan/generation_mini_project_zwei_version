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
    
    def execute_leave_open(self, sql):
        self.cur.execute(sql)


def show_db_data(selection):
    try:
        db = HelperDB()
        rows = db.fetch_all(f'SELECT * FROM {selection}')
        print('inside the func', rows)
        #get the table names
        column_names = db.get_column_names(selection)
        print('\n')
        for row in rows:
            print(f'{column_names[0]}: {row[0]}, {column_names[1]}: {row[1]}, {column_names[2]}: {row[2]}')

    except Exception as error:
        print('Cannot load database, check your setup', error)
    else:
        if db.conn.open:
            db.disconnect_database()

        return rows

    return []

def add_to_db(selection, new_value):
    try:
        db = HelperDB()
        if selection == 'orders':
            column_names_cus = db.get_column_names('customer_detail')
            column_names_ord = db.get_column_names('orders')

            db.set_up_db_connection()
            sql1 = f'INSERT INTO customer_detail ( {column_names_cus[1]},{column_names_cus[2]},{column_names_cus[3]} )' + f' VALUES (\"{new_value[0]}\",\"{new_value[1]}\",\"{new_value[2]}\");'
            db.execute_leave_open(sql1)
            db.execute_leave_open('SELECT LAST_INSERT_ID()')
            get_created_cust_id = int(db.cur.fetchall()[0][0])

            for product_id in new_value[-1]:
                sql2 = f' INSERT INTO orders ( {column_names_ord[1]},{column_names_ord[2]},{column_names_ord[3]},{column_names_ord[4]} )' + f' VALUES ({get_created_cust_id}, {new_value[3]},{new_value[4]},{product_id} );'
                db.execute_leave_open(sql2)
        else:
            column_names = db.get_column_names(selection)
            db.execute_operation(
                f'INSERT INTO {selection} ( {column_names[1]},{column_names[2]} )'
                + f' VALUES ( \"{new_value[0]}\",{new_value[1]} );'
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
        previous_input_index = input_helper(promt_msg, [], set_int=True, isLoop=True)
        for col_name in column_names:
            new_input = input(f'New value for {col_name}: ')
            if new_input == "":
                continue
            else:
                if col_name not in ['price']:
                    new_input = f'\"{new_input}\"'

                sql = f'UPDATE {selection} SET {col_name} = {new_input} WHERE id = {previous_input_index}'
                db.execute_operation(sql)

    except Exception as error:
        print('Cannot update to Database', error)
    else:
        print('\nData has been updated!\n')
        if db.conn.open:
            db.disconnect_database()


def delete_to_db(selection, index):
    try:
        db = HelperDB()
        db.execute_operation(f'DELETE FROM {selection} WHERE id = {index};')
        print(f'Index entry: {index} has now been deleted!\n')
    except Exception as error:
        print('Cannot delete data from the database. ' + str(error.args[1]))
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