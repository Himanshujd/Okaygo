from utilities import DbManager

DbManager.createDbConnection()
data = DbManager.getMySqlQuery("select tutorial_author from selenium where tutorial_id = 2")
print(data)