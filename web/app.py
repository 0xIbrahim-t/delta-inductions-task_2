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

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/core', methods=['GET', 'POST'])
def core_dashboard():
    if 'user_type' in session and session['user_type'] == 'core':
        if request.method == 'POST':
            if 'mentee' in request.form:
                mentee = request.form.get('mentee')
                return redirect(url_for('mentee_dashboard_other', role='core', mentee=mentee))
            elif 'mentor' in request.form:
                mentor = request.form.get('mentor')
                return redirect(url_for('mentor_dashboard_other', mentor=mentor))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM web_users WHERE user_type = 'mentee'")
        mentees = cursor.fetchall()
        cursor.execute("SELECT name FROM web_users WHERE user_type = 'mentor'")
        mentors = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('core.html', mentees=[d[0] for d in mentees], mentors=[a[0] for a in mentors])
    return redirect(url_for('index'))
    
@app.route('/mentor', methods=['GET', 'POST'])
def mentor_dashboard():
    if 'user_type' in session and session['user_type'] == 'mentor':
        if request.method == 'POST':
            mentee = request.form.get('mentee')
            return redirect(url_for('mentee_dashboard_other', role='mentor', mentee=mentee))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (session['username'],))
        mentees = cursor.fetchone()[0]
        allocated_mentees = mentees.split(',')
        cursor.execute("SELECT domain_1 FROM web_users WHERE username = %s", (session['username'],))
        domain = cursor.fetchone()[0]
        cursor.execute("SELECT rollnumber FROM web_users WHERE username = %s", (session['username'],))
        mentor_capacity = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return render_template('mentor.html', name=session['username'], allocated_mentees=allocated_mentees, domain=domain, mentor_capacity=mentor_capacity)
    return redirect(url_for('index'))

@app.route('/core/<mentor>', methods=['GET', 'POST'])
def mentor_dashboard_other(mentor):
    if 'user_type' in session and session['user_type'] == 'core':
        if request.method == 'POST':
            mentee = request.form.get('mentee')
            return redirect(url_for('mentee_dashboard_others', role=mentor, mentee=mentee))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (mentor,))
        mentees = cursor.fetchone()[0]
        allocated_mentees = mentees.split(',')
        cursor.execute("SELECT domain_1 FROM web_users WHERE username = %s", (mentor,))
        domain = cursor.fetchone()[0]
        cursor.execute("SELECT rollnumber FROM web_users WHERE username = %s", (mentor,))
        mentor_capacity = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return render_template('mentor.html', name=mentor, allocated_mentees=allocated_mentees, domain=domain, mentor_capacity=mentor_capacity)
    return redirect(url_for('index'))


@app.route('/mentee')
def mentee_dashboard():
    if 'user_type' in session and session['user_type'] == 'mentee':
        mentee = session['username']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT usertype FROM web_users WHERE username = %s", (session['username'],))
        user_type = cursor.fetchone()[0]
        cursor.execute("SELECT rollnumber FROM web_users WHERE username = %s", (session['username'],))
        rollnumber = cursor.fetchone()[0]
        cursor.execute("SELECT allocated_mentor FROM web_users WHERE username = %s", (session['username'],))
        allocated_mentor = cursor.fetchone()[0]
        cursor.execute("SELECT domain_1 FROM web_users WHERE username = %s", (session['username'],))
        domain_1 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (session['username'],))
        domain_2 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_3 FROM web_users WHERE username = %s", (session['username'],))
        domain_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_submitted WHERE Task_number = 1")
        sysad_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_submitted WHERE Task_number = 1")
        web_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_submitted WHERE Task_number = 1")
        app_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_submitted WHERE Task_number = 2")
        sysad_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_submitted WHERE Task_number = 2")
        web_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_submitted WHERE Task_number = 2")
        app_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_submitted WHERE Task_number = 3")
        sysad_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_submitted WHERE Task_number = 3")
        web_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_submitted WHERE Task_number = 3")
        app_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_completed WHERE Task_number = 1")
        sysad_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_completed WHERE Task_number = 1")
        web_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_completed WHERE Task_number = 1")
        app_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_completed WHERE Task_number = 2")
        sysad_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_completed WHERE Task_number = 2")
        web_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_completed WHERE Task_number = 2")
        app_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {session['username']}_task_completed WHERE Task_number = 3")
        sysad_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {session['username']}_task_completed WHERE Task_number = 3")
        web_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {session['username']}_task_completed WHERE Task_number = 3")
        app_completed_3 = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return render_template('mentee.html', mentee=mentee, rollnumber=rollnumber, allocated_mentor=allocated_mentor domain_1=domain_1, domain_2=domain_2, domain_3=domain_3, sysad_submitted_1=sysad_submitted_1, web_submitted_1=web_submitted_1, app_submitted_1=app_submitted_1, sysad_submitted_2=sysad_submitted_2, web_submitted_2=web_submitted_2, app_submitted_2=app_submitted_2, sysad_submitted_3=sysad_submitted_3, web_submitted_3=web_submitted_3, app_submitted_3=app_submitted_3, sysad_completed_1=sysad_completed_1, web_completed_1=web_completed_1, app_completed_1=app_completed_1, sysad_completed_2=sysad_completed_2, web_completed_2=web_completed_2, app_completed_2=app_completed_2, sysad_completed_3=sysad_completed_3, web_completed_3=web_completed_3, app_completed_3=app_completed_3)
    return redirect(url_for('index'))

@app.route('/<role>/<mentee>')
def mentee_dashboard_other(mentee):
    if 'user_type' in session and session['user_type'] in ['core', 'mentor']:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT usertype FROM web_users WHERE username = %s", (mentee,))
        user_type = cursor.fetchone()[0]
        cursor.execute("SELECT rollnumber FROM web_users WHERE username = %s", (mentee,))
        rollnumber = cursor.fetchone()[0]
        cursor.execute("SELECT allocated_mentor FROM web_users WHERE username = %s", (mentee,))
        allocated_mentor = cursor.fetchone()[0]
        cursor.execute("SELECT domain_1 FROM web_users WHERE username = %s", (mentee,))
        domain_1 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (mentee,))
        domain_2 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_3 FROM web_users WHERE username = %s", (mentee,))
        domain_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 1")
        sysad_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 1")
        web_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 1")
        app_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 2")
        sysad_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 2")
        web_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 2")
        app_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 3")
        sysad_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 3")
        web_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 3")
        app_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 1")
        sysad_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 1")
        web_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 1")
        app_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 2")
        sysad_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 2")
        web_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 2")
        app_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 3")
        sysad_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 3")
        web_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 3")
        app_completed_3 = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return render_template('mentee.html', mentee=mentee, rollnumber=rollnumber, allocated_mentor=allocated_mentor domain_1=domain_1, domain_2=domain_2, domain_3=domain_3, sysad_submitted_1=sysad_submitted_1, web_submitted_1=web_submitted_1, app_submitted_1=app_submitted_1, sysad_submitted_2=sysad_submitted_2, web_submitted_2=web_submitted_2, app_submitted_2=app_submitted_2, sysad_submitted_3=sysad_submitted_3, web_submitted_3=web_submitted_3, app_submitted_3=app_submitted_3, sysad_completed_1=sysad_completed_1, web_completed_1=web_completed_1, app_completed_1=app_completed_1, sysad_completed_2=sysad_completed_2, web_completed_2=web_completed_2, app_completed_2=app_completed_2, sysad_completed_3=sysad_completed_3, web_completed_3=web_completed_3, app_completed_3=app_completed_3)
    return redirect(url_for('index'))

@app.route('/core/<role>/<mentee>')
def mentee_dashboard_others(mentee):
    if 'user_type' in session and session['user_type'] == 'core':
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT rollnumber FROM web_users WHERE username = %s", (mentee,))
        rollnumber = cursor.fetchone()[0]
        cursor.execute("SELECT allocated_mentor FROM web_users WHERE username = %s", (mentee,))
        allocated_mentor = cursor.fetchone()[0]
        cursor.execute("SELECT domain_1 FROM web_users WHERE username = %s", (mentee,))
        domain_1 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (mentee,))
        domain_2 = cursor.fetchone()[0]
        cursor.execute("SELECT domain_3 FROM web_users WHERE username = %s", (mentee,))
        domain_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 1")
        sysad_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 1")
        web_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 1")
        app_submitted_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 2")
        sysad_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 2")
        web_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 2")
        app_submitted_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_submitted WHERE Task_number = 3")
        sysad_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_submitted WHERE Task_number = 3")
        web_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_submitted WHERE Task_number = 3")
        app_submitted_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 1")
        sysad_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 1")
        web_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 1")
        app_completed_1 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 2")
        sysad_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 2")
        web_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 2")
        app_completed_2 = cursor.fetchone()[0]
        cursor.execute("SELECT Sysad FROM {mentee}_task_completed WHERE Task_number = 3")
        sysad_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT Web FROM {mentee}_task_completed WHERE Task_number = 3")
        web_completed_3 = cursor.fetchone()[0]
        cursor.execute("SELECT App FROM {mentee}_task_completed WHERE Task_number = 3")
        app_completed_3 = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return render_template('mentee.html', mentee=mentee, rollnumber=rollnumber, allocated_mentor=allocated_mentor, domain_1=domain_1, domain_2=domain_2, domain_3=domain_3, sysad_submitted_1=sysad_submitted_1, web_submitted_1=web_submitted_1, app_submitted_1=app_submitted_1, sysad_submitted_2=sysad_submitted_2, web_submitted_2=web_submitted_2, app_submitted_2=app_submitted_2, sysad_submitted_3=sysad_submitted_3, web_submitted_3=web_submitted_3, app_submitted_3=app_submitted_3, sysad_completed_1=sysad_completed_1, web_completed_1=web_completed_1, app_completed_1=app_completed_1, sysad_completed_2=sysad_completed_2, web_completed_2=web_completed_2, app_completed_2=app_completed_2, sysad_completed_3=sysad_completed_3, web_completed_3=web_completed_3, app_completed_3=app_completed_3)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
