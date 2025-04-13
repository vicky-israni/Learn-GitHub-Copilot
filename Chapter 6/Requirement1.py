from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for simplicity
users = {}

@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome, {session['user']}! <a href='/logout'>Logout</a>"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = generate_password_hash(request.form['password'])
        profile_picture = request.files['profile_picture']

        if email in users:
            return "User already exists. Please log in."

        # Save profile picture
        profile_picture_path = os.path.join('static/uploads', profile_picture.filename)
        profile_picture.save(profile_picture_path)

        # Save user data
        users[email] = {
            'name': name,
            'phone': phone,
            'password': password,
            'profile_picture': profile_picture_path
        }
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.get(email)
    if user and check_password_hash(user['password'], password):
        session['user'] = user['name']
        return redirect(url_for('home'))
    return "Invalid credentials. Please try again."

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)