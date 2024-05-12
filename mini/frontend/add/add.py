import os
import zipfile
import datetime
import tempfile

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def append_to_file(data, file_path='C:/me/mini project/mini/history.txt'):
    with open(file_path, 'a') as file:
        file.write('\n' + data)

def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        append_to_file(f"File deleted {get_current_time()} : {file_path}")

def zip_folder(directory_path='C:/me/mini project/mini/frontend/add/saved', output_zip_path='C:/me/mini project/mini/frontend/add/added/saved.zip'):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, directory_path))
    append_to_file(f"files added {get_current_time()} ")

def unzip_response(response):
    if response is None or not response.startswith('PK'):
        return
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(response.encode('utf-8'))
        temp_file.flush()
        unzip_folder(temp_file.name)
        append_to_file(f'pull Sucessful at {get_current_time()} ')
        return True

def unzip_folder(data, extract_path='C:/me/mini project/mini/frontend/add/saved'):
    # Open the zip file using the ZipFile constructor
    with zipfile.ZipFile('C:/me/mini project/mini/frontend/add/added/saved.zip', 'r') as zip_file:
        zip_file.extractall(extract_path)