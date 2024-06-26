import mysql.connector
import os

mentor = os.getenv('mentor')
mentee = os.getenv('mentee')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="Task_db")
mycursor = mydb.cursor()

mycursor.execute("SELECT domain_2 FROM web_users WHERE username = %s", (mentor,))
allocated = mycursor.fetchone()[0]

mycursor.execute("UPDATE web_users SET allocated_mentor = %s WHERE username = %s", (mentor, mentee))

allocated = allocated + mentee

mycursor.execute("UPDATE web_users SET domain_2 = %s WHERE username = %s", (allocated, mentor))

mydb.commit()
mycursor.close()
mydb.close()
