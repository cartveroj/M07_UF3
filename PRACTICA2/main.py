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
    print("Insertamos un registro")
   # read()

    #Cambiamos el nombre del registro del registro id=1

  #  update_data("Francisca")
  #  read()

    #Borramos el registro
  #  delete()
   
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()