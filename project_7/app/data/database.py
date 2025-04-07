import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deepak",
        database="project_management_db2"
    )
    return conn

