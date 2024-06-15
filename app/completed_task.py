import mysql.connector
import os

name = os.getenv('USER')
completed_Task = os.getenv('completedTask')
allocated_domain = os.getenv('allocatedDomain')
name = os.getenv('allocated_mentee')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="Task_db")
mycursor = mydb.cursor()

for num in [0, 1, 2]:
    mycursor.execute(f"UPDATE {name}_task_completed SET {allocated_domain} = '{completed_Task[num]}' WHERE Task_number = {num + 1};")

mycursor.close()
mydb.close()
