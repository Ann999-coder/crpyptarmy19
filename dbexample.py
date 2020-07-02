import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)
mycur=mydb.cursor();
#cp=mycur.execute("sql")
print("success")