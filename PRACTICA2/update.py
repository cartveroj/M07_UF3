
'''
Archivo que contiene una funcion que actualiza una columna
NAME de la tabla USERS 
'''
from conecction import *

def update_data(name):
    
    sql_update ="UPDATE USERS SET user_name = %s WHERE user_id = '1'"
    print(sql_update)
    connection.execute(sql_update, (name,)) 
    conn.commit()
    resultado = connection.rowcount
    print("id moficada ", resultado, "Actualizada correctamente")

