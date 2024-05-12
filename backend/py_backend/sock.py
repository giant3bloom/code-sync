
import os
import shutil
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

def del_zip():
    zip_file = 'saved.zip'
    file_path = os.path.join('C:/me/mini project/backend/py_backend/data/folder/old', zip_file)
    if os.path.isfile(file_path):
        os.remove(file_path)

def move_folder():
    src_dir = 'C:/me/mini project/backend/py_backend/data/folder/current'
    dst_dir = 'C:/me/mini project/backend/py_backend/data/folder/old'
    file_name = 'saved.zip'
    src_file = os.path.join(src_dir, file_name)
    dst_file = os.path.join(dst_dir, file_name)
    os.chdir(src_dir)
    del_zip()
    dst_dir = os.path.join(dst_dir, 'saved.zip')
    if os.path.isfile(src_file) :
        shutil.move(file_name, dst_dir)

def save_folder(data):
    dist = 'C:/me/mini project/backend/py_backend/data/folder/current/saved.zip'
    with open(dist, 'wb') as file:
        file.write(data.encode('utf-8', 'ignore'))
    return file

def push_zip(name, data):
    move_folder()
    save_folder(data)
    append_to_file(f'Zip file has been pushed at {get_current_time()} by {name}')
    return pack('push', True) 


def pull_zip(name, sock, file_path = 'C:/me/mini project/backend/py_backend/data/folder/current/saved.zip'):
    with open(file_path, 'rb') as file:
        data = file.read()
        sock.sendall(pack('pull', data))
    append_to_file(f'zip file has been pulled at {get_current_time()} by {name}')


