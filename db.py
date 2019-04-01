import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sillyfish959",
  passwd="123456"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE My_House")
mycursor.execute("select User from mysql.user")
