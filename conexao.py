import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="5.1179.137.175",
    user="admin",
    password="admin123",
    database="africa"
  )
  return mydb