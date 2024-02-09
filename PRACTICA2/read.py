'''
Archivo que contiene una funcion que recupera todos los 
datos de la tabla USERS
'''

from conecction import *

def read():
    query ='''SELECT * FROM USERS'''
    print(query)
    connection.execute(query)
    result = connection.fetchall()
    print(result)
    for dato in result:
        print("Id:",dato[0])
        print("Name:",dato[1])
        print("Surname:",dato[2])
        print("Age:",dato[3])
        print("Email:",dato[4])


read()
 