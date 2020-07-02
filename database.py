import mysql.connector



mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="army"
)

mycursor = mydb.cursor()

sql = "select password from login where userid=%s"
adr = ("23",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchone()

for x in myresult:
  print(x)