import socket
import datetime
from frontend.request.jser import rj, mkj
from frontend.add.add import unzip_response

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

def append_to_file(data, file_path='C:/me/mini project/mini/history.txt'):
    with open(file_path, 'a') as file:
        file.write('\n' + data)

def sent(name, request, data):
    data = mkj(name,request, data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('bloom', 12345))

    if request=='login' or request=='signup':
        s.sendall(data)
        response = rj(s.recv(1024).decode("utf-8"))

        if request=='login' :
            if response == True :
                append_to_file(f'Login Successful at {get_current_time()} ')
            else:
                append_to_file(f'Login Failed at {get_current_time()} ')
        elif request=='signup' :
            if response == True:
                append_to_file(f'Signup Successful at {get_current_time()} ')
            else:
                append_to_file(f'Signup failed at {get_current_time()} ')
        return response

    if request=='push':
        s.sendall(data)
        response = rj(s.recv(1024).decode("utf-8"))
        if response==True :
            append_to_file(f'push Sucessful at {get_current_time()} ')
        else :
            append_to_file(f'push failed at {get_current_time()} ')
        return response


    # Example usage:
    if request == 'pull':
        s.sendall(data)
        response = rj(s.recv(1000000000).decode('utf-8'))
        if unzip_response(response):
            append_to_file(f'pull Sucessful at {get_current_time()} ')
            return True
        else:
            append_to_file(f'pull failed at {get_current_time()} ')
            return False
    
    if request == 'end' : 
        s.sendall(data)
        append_to_file(f'server closed by {name} at {get_current_time()} ')
        return True

    s.close()
