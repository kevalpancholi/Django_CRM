import pymysql
dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'your_new_password'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("DROP DATABASE IF EXISTS pharmx")

# Create a database
cursorObject.execute("CREATE DATABASE pharmx")

print('All done!')
# cursorObject.close()
# dataBase.close()