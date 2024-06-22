import mysql.connector
import os

name = os.getenv('USER')
submitted_Task = os.getenv('submittedTask')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="Task_db")
mycursor = mydb.cursor()

for num in [0, 1, 2]:
    mycursor.execute(f"UPDATE {name}_task_submitted SET Sysad = '{submitted_Task[num]}' WHERE Task_number = {num + 1};")
    mycursor.execute(f"UPDATE {name}_task_submitted SET Web = '{submitted_Task[num + 3]}' WHERE Task_number = {num + 1};")
    mycursor.execute(f"UPDATE {name}_task_submitted SET App = '{submitted_Task[num + 6]}' WHERE Task_number = {num + 1};")

mycursor.close()
mydb.close()
