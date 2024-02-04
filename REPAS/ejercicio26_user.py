'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 26
##########################################
FUNCIONS
Crear un arxiu de nom user.py. 
En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json


'''
from user import user

u1 = user("Veronica", "Cartagena", "30", "12345", "vcj@gmail.com","654123") #instanciamos la clase

u1.salutacio()
json_user = u1.to_dict()
print(json_user)


