
from time import sleep
from sock import append_to_file, get_current_time

def start():
    print("Server Starting", end="")
    for _ in range(5):
        sleep(0.5)
        print('.', end="")
    print()
    append_to_file(f'server start at {get_current_time()} ')

def end():
    print('connection Closing', end='')
    for _ in range(5):
        sleep(0.5)
        print('.', end='')
    print()

if __name__ == '__main__':
    
    start()
    end()
