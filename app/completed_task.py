import mysql.connector
import os

name = os.getenv('USER')
completed_Task = os.getenv('completedTask')
db_host = os.getenv('dbHost')
allocated_domain = os.getenv('allocatedDomain')
name = os.getenv('allocated_mentee')

mydb = mysql.connector.connect(host=db_host,user="username",password="password",database="Task_db")
mycursor = mydb.cursor()

mycursor.execute(f"DROP TABLE IF EXISTS {name}_task_completed")
mycursor.execute(f"create table {name}_task_completed (Task_number INT, Sysad VARCHAR(1), Web VARCHAR(1), App VARCHAR(1))")

for num in [0, 1, 2]:
    mycursor.execute(f"INSERT INTO {name}_task_completed (Task_number, {allocated_domain}) Values ({num}, {submitted_Task[num]}, {submitted_Task[num+3]}, {submitted_Task[num+6]})")
