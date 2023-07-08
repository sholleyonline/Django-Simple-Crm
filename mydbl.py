import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sholleyjava'
)

# Prepare a cursor object
cursorObject = database.cursor()

#Create database
cursorObject.execute("CREATE DATABASE django_simplecrm")
