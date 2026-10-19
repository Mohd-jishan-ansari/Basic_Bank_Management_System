import mysql.connector as myconn;

def connect():
    return myconn.connect(
        host = "localhost",
        user="root",
        password ="zee1$",
        database ="bank_system"
    )