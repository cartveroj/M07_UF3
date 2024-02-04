'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 25
##########################################
FUNCIONS
Crear un arxiu de nom vehicle.py. 
En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

'''
from vehicle import vehicle

v1 = vehicle("negro", "mustan", "2023", "4jhc", "4","hibrido") #instanciamos la clase

v1.parts()
json_vehicle = v1.to_dict()
print(json_vehicle)

