import mysql.connector as conn

def conectar():
    return conn.connect(
        host='localhost',
        user='root',
        password='',
        database='consumiveis_impressoras'
    )
