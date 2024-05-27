import mysql.connector


def createDbConnection():
    global mydb
    mydb = mysql.connector.connect(

        host="localhost",
        user="root",
        password="selenium",
        database="pydb"

    )


def getMySqlQuery(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    return myresult[0]
