
# --------------------------------------------------------------------------------
#                                    main
# --------------------------------------------------------------------------------
import consoler as cs
import socket 
import datetime
from jser import unpack
from Authenticate import sign_up, login
from sock import pull_zip, push_zip

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

def append_to_file(data, file_path='C:/me/mini project/backend/py_backend/data/history.txt'):
    with open(file_path, 'a') as file:
        file.write('\n' + data)
        print(data)

def reciver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 12345))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        filename = clientsocket.recv(1000000000)
        filename = filename.decode("utf-8")
        filename = unpack(filename)

        name = filename['name']
        request = filename['request']
        data = filename['data']
        if request=='signup':
            response = sign_up(data['name'], data['password'])
            clientsocket.sendall(response)
        elif request=='login':
            response = login(data['name'], data['password'])
            clientsocket.sendall(response)
        elif request=='push':
            clientsocket.sendall(push_zip(name, data))
        elif request=='pull':
            pull_zip(name, clientsocket)
        elif request=='end' :
            cs.end()
            clientsocket.close()
        
        
def main():
    cs.start()
    reciver()


if __name__ == '__main__' :

    main()