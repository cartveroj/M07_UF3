import psycopg2
print(psycopg2.__file__)

conn = psycopg2.connect(
    database='postgresP2',
    user='veronica',
    password='pirineus',
    host='localhost',
    port='5432'
)

connection = conn.cursor()
print(connection)