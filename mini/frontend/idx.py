from frontend.add import add as ad
from frontend.request.sock import sent, append_to_file, get_current_time

name = None

def add():
    ad.zip_folder()
    return True
    
def signup(name1, password):
    global name
    data = {}
    data['name'] = name1
    global name
    name = name1
    data['password'] = password
    response = sent(name, 'signup', data)
    if response :
        append_to_file(f'signup at {get_current_time()} ')
    else :
        append_to_file(f'failed to signup at {get_current_time()} ')
    return response

def login(name1, password):
    global name 
    name = name1
    data = {}
    data['name'] = name1
    data['password'] = password

    response = sent(name, 'login', data)
    if response :
        append_to_file(f'login at {get_current_time()} ')
    else :
        append_to_file(f'failed to login at {get_current_time()} ')
    return response

def pull():
    global name
    response = sent(name, 'pull', None)
    if response :
        append_to_file(f'pulled at {get_current_time()} ')
    else:
        append_to_file(f'failed to pull at {get_current_time()} ')
    return response

def end():
    global name
    return sent(name, 'end', None)
        
def push(file_path='C:/me/mini project/mini/frontend/add/added/saved.zip'):
    global name
    with open(file_path, 'rb') as file:
        data = file.read()
    response = sent(name, 'push', data)
    if response:
        append_to_file(f'pushed at {get_current_time()} ')
    else:
        append_to_file(f'failed to push at {get_current_time()} ')
    return response
