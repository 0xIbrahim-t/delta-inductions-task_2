import mysql.connector
from flask import Flask, request, render_template, redirect, url_for, session, flash

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(host='db', user='username', password='password', database='Task_db')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT usertype FROM web_users WHERE username = %s", (username,))
        user_type = cursor.fetchone()[0]
        cursor.execute("SELECT password FROM web_users WHERE username = %s", (username,))
        real_password = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        if password == real_password:
            session['user_type'] = user_type
            session['username'] = username
            if user_type == 'core':
                return redirect(url_for('core_dashboard'))
            elif user_type == 'mentor':
                return redirect(url_for('mentor_dashboard'))
            elif user_type == 'mentee':
                return redirect(url_for('mentee_dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return redirect(url_for('index'))
