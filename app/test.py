import mysql.connector
import os

name = os.getenv('USER')

mydb = mysql.connector.connect(host=db_host,user="username",password="password",database="Task_db")
mycursor = mydb.cursor()
print("database connected")

mycursor.execute(f"create table {name}_task_submitted (Task_number INT, Sysad VARCHAR(1), Web VARCHAR(1), App VARCHAR(1))")
mycursor.execute(f"create table {name}_task_completed (Task_number INT, Sysad VARCHAR(1), Web VARCHAR(1), App VARCHAR(1))")

mycursor.execute("SHOW TABLES")
databases = mycursor.fetchall()
for db in databases:
    print(db[0])

mycursor.close()
mydb.close()
