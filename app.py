from flask import Flask, render_template, request

app = Flask(__name__)

correct_username = "mohammad" 
correct_password = "2468"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == correct_username and password == correct_password:
        return render_template('success.html', username=username)
    else:
        return render_template('failure.html')
    
if __name__ == "__main__":
    app.run(debug=True)