import mysql.connector
import os

name = os.getenv('mentee_db')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="Task_db")
mycursor = mydb.cursor()


mycursor.execute(f"SHOW TABLES LIKE '{{name}_task_submitted}'")
result = mycursor.fetchone()

if result:
    pass
else:
    mycursor.execute(f"create table {name}_task_submitted (Task_number INT, Sysad VARCHAR(1), Web VARCHAR(1), App VARCHAR(1))")
    for num in [0, 1, 2]:
        mycursor.execute(f"INSERT INTO {name}_task_submitted (Task_number, Sysad, Web, App) Values ({num + 1}, "n", "n", "n")")

mycursor.close()
mydb.close()
