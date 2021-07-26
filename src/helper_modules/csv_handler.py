import csv
import json

from .file_handler import set_up_path

def load_field_names(name):
    list_of_filednames = {
        "fake_data":['name', 'price'],
        "product": ['name', 'price'],
        "courier": ['name', 'phone'],
        "orders": ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items']
    }
    return list_of_filednames.get(name)

def write_csv(data, filename):
    error_msg = 'The data is not formated correctly'
    if isinstance(data, list):
        pathway = set_up_path(filename)
        # name without extension
        short_filename = filename.split('.')[0]
        fieldnames = load_field_names(short_filename)
        print('pathway', pathway)
        with open(pathway, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=",")
            
            writer.writeheader()
            for each_data in data:
                if isinstance(each_data, dict):
                    print('testing', each_data)
                    writer.writerow(each_data)
                else:
                    print(error_msg)
                    return error_msg

    else:
        print(error_msg)
        return error_msg

def read_csv(filename):
    pathway = set_up_path(filename)
    short_filename = filename.split('.')[0]
    store = []
    try:
        with open(pathway, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            
            for row in csv_reader:
                store.append(row)
        return convert_to_correct_type(store, short_filename)
    except FileNotFoundError as error:
        print(error.args[1])
        return []


def convert_to_correct_type(data_storage, filename):
    try:
        if filename == 'product':
            for data in data_storage:
                for key, value in data.items():
                    if key == 'price':
                        data[key] = float(value)
            return data_storage
        elif filename == 'orders':
            for data in data_storage:
                for key, value in data.items():
                    if key == 'courier':
                        data[key] = int(value)
                    if key == 'items':
                        data[key] = json.loads(value)
            return data_storage
        else:
            return data_storage
    except Exception as error:
        return error