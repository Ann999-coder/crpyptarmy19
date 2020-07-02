import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
print("success")