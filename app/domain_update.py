import mysql.connector
import os

pref = os.getenv('pref_no')
mentee = os.getenv('$USER')
pref_1 = os.getenv('pref1')
pref_2 = os.getenv('pref2')
pref_3 = os.getenv('pref3')

mydb = mysql.connector.connect(host="db",user="username",password="password",database="Task_db")
mycursor = mydb.cursor()

if int(pref) == 1:
  mycursor.execute("UPDATE web_users SET domain_1 = %s WHERE username = %s", (pref_1, mentee))
elif int(pref) == 2:
  mycursor.execute("UPDATE web_users SET domain_1 = %s WHERE username = %s", (pref_1, mentee))
  mycursor.execute("UPDATE web_users SET domain_2 = %s WHERE username = %s", (pref_2, mentee))
elif int(pref) == 2:
  mycursor.execute("UPDATE web_users SET domain_1 = %s WHERE username = %s", (pref_1, mentee))
  mycursor.execute("UPDATE web_users SET domain_2 = %s WHERE username = %s", (pref_2, mentee))
  mycursor.execute("UPDATE web_users SET domain_3 = %s WHERE username = %s", (pref_3, mentee))


mydb.commit()
mycursor.close()
mydb.close()
