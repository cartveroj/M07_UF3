from conecction import *
try:
    print("Hola")
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()