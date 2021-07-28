import json, os

from helper_modules.file_handler import set_up_path

# first_data = [
#     {
#     "customer_name": "John",
#     "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
#     "customer_phone": "0789887334",
#     "courier": 2,
#     "status": "preparing"
#     }
# ]
status = ["preparing", "out-for-delivery", "delivered"]

# def initialize():
#     pathway = set_up_path(filename)
#     with open(pathway, mode="w") as json_file:
#         json.dump(first_data, json_file, indent = 4)

def read_orders(filename):
    pathway = set_up_path(filename)
    with open(pathway, mode='r') as json_file:
        return json.load(json_file)

def write_orders(new_data, filename):
    pathway = set_up_path(filename)
    with open(pathway, mode='w') as json_file:
        json.dump(new_data, json_file, indent = 4)
