import mysql.connector
import os

name = os.getenv('USER')
submitted_Task = os.getenv('submittedTask')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="db_name")
mycursor = mydb.cursor()

mycursor.execute(f"DROP TABLE IF EXISTS {name}_task_submitted")
mycursor.execute(f"create table {name}_task_submitted (Task_number INT, Sysad VARCHAR(1), Web VARCHAR(1), App VARCHAR(1))")

for num in [0, 1, 2]:
    mycursor.execute(f"INSERT INTO {name}_task_submitted (Task_number, Sysad, Web, App) Values ({num + 1}, {submitted_Task[num]}, {submitted_Task[num+3]}, {submitted_Task[num+6]})")

mycursor.close()
mydb.close()
