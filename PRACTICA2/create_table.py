
'''
Archivo que contiene una funcion que crear una tabla
en la base de datos
'''
from conecction import *

def create_table():
    
    sql ='''CREATE TABLE IF NOT EXISTS USERS (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_surname VARCHAR(255) NOT NULL,
            user_age BIGINT NOT NULL,
            user_email VARCHAR NOT NULL
            )
    '''
    print(sql)
    connection.execute(sql)
    print(connection)
    conn.commit()

