from flask import Flask, render_template, jsonify, request, url_for
import os
import subprocess
from frontend import idx 

app = Flask(__name__)

@app.route('/add')
def add():
    return jsonify(idx.add())

@app.route('/push')
def push():
    return jsonify(idx.push())

@app.route('/pull')
def pull():
    return jsonify(idx.pull())

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    return jsonify(idx.login(name, password))

@app.route('/chglogin')
def chglogin():
    return render_template('login.html')

@app.route('/chgsignup')
def chgsignup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    return jsonify(idx.signup(name, password))

@app.route('/get_files')
def get_files():
    folder_path = 'C:/me/mini project/mini/frontend/add/saved'
    files = os.listdir(folder_path)
    return jsonify(files)

@app.route('/execute_code', methods=['POST'])
def execute_code():
    # Get the code from the request
    code = request.json.get('code')
    name = request.json.get('name')
    path = 'c:/me/mini project/mini/frontend/add/saved/{}.py'.format(name)
    # Write the code to a temporary file
    with open(path, 'w') as file:
        file.write(code)
    # Execute the code using the Python interpreter
    process = subprocess.Popen(['python', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    # Terminate the subprocess
    process.terminate()
    # Return the output to the frontend
    return jsonify(output=stdout)

@app.route('/')
def index():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=False)

