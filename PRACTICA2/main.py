'''
Archivo principal que ejecuta todas las funciones
'''

from conecction import *
from create_table import *
from create import *
from read import *
from update import *
from delete import *

try:
    #Creamos la tabla
    print("Creamos la tabla USERS")
    create_table()

    #Insertamos datos
    print("Insertamos un registro")
    create()

    #Recuperamos datos
    print("Recuperamos el registro")
    read()

    #Cambiamos el nombre del registro del registro id=1
    print("Modificamos el nombre")
    update_data("Francisca")
    read()

    #Borramos el registro
    print("Eliminamos el registro")
    delete()
   
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    #Cerramos la conección
    connection.close()
    conn.close() 