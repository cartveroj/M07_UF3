'''
Archivo que contiene la coneccion con la base de datos
'''
import psycopg2

conn = psycopg2.connect(
    database='postgresP2',
    user='veronica',
    password='pirineus',
    host='localhost',
    port='5432'
)
connection = conn.cursor()
print(connection)