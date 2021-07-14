import os

def set_up_path(filename):
    """Set the path to folder containing the data
    
    Args:
    filename (str): The name of file with it's format ("product.txt" or "courier.txt")
    
    Returns:
    str: String which contains the absolute pathway of the folder containing the data
    """

    os.path.abspath(__file__)
    # Get the directory of the data file
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    # data_path = f"generation_mini_project\data\{filename}"
    data_path = f"data/{filename}"
    abs_file_path = os.path.join(fileDir, data_path)
    return abs_file_path

def read_data(file_name):
    """Loads the data from the data folder and returns that data
    
    Args:
    filename (str): The name of file with it's format ("product.txt" or "courier.txt")
    
    Returns:
    list: List of cleaned data
    """

    pathway = set_up_path(file_name)
    # print(pathway)
    with open(pathway, 'r') as file:
        data = file.readlines()
        data = [product.strip() for product in data]
        return data

def append_data(data, file_name):
    """Adds the new data to end of the text file
    
    Args:
    data (str): The name of the data being added (product or courier)
    file_name(str): The name of file which is going to be opened ("product.txt" or "courier.txt")
    
    """
    
    pathway = set_up_path(file_name)
    with open(pathway, 'a') as file:
        file.writelines(f'{data}\n')


def new_write(data, file_name):
    """Writes the whole list of the new updated data into a text file
    
    Args:
    data (list): List of new updated data for the product or courier
    file_name(str): The name of file which is going to be opened ("product.txt" or "courier.txt")
    
    """
    
    pathway = set_up_path(file_name)
    with open(pathway, 'w') as file:
        for d in data:
            file.write(f'{d}\n')