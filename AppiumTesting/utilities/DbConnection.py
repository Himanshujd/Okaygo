import mysql.connector


mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="selenium",
    database="pydb"


)

mycursor = mydb.cursor()

mycursor.execute("select tutorial_author from selenium where tutorial_id = 2")

# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)


myresult = mycursor.fetchone()
print(myresult[0])