import mysql


database = mysql.connector.connect(
    host = 'localhost',
    user = 'dbadmin',
    passwd = 'password123'
)

# Cursor Object

cursorObject = database.cursor()

# Create database

cursorObject.execute("create database crmdb")

print("All Good!")