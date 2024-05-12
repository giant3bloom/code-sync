
import csv
import datetime
from jser import pack



def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

def append_to_file(data, file_path='C:/me/mini project/backend/py_backend/data/history.txt'):
    with open(file_path, 'a') as file:
        file.write('\n' + data)
        print(data)


def check_data_in_same_row(file_path, data1, data2):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if data1 in row and data2 in row:
                return True
        return False

def login(name, password):
    if check_data_in_same_row('C:/me/mini project/backend/py_backend/data/users.csv', name, password):
        append_to_file(f'{name} logined at {get_current_time() } ')
        return pack('login', True) 
    else:
        append_to_file(f'{name} login failed at {get_current_time()} ')
        return pack('login', False)
    

def sign_up(name, password):
    file_path = 'C:/me/mini project/backend/py_backend/data/users.csv'
    if not (check_data_in_same_row(file_path, name, password)) : 
        # Open the CSV file in write mode
        with open(file_path, mode="a", encoding="utf-8") as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            data = [name, password]
            # Write the header row
            writer.writerow(data)
        append_to_file(f'{name} signed at {get_current_time()}')
        return pack('sign_up', True)
    else :
        append_to_file(f'{name} sign up failed at {get_current_time()} ')
        return pack('sign_up', False)

