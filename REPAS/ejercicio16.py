'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 16
##########################################
Demanar a l’usuari una frase. 
El programa eliminarà els espais i s'afegirà a una tupla. 
Mostrar per pantalla el contingut de la tupla.

'''

frase = input("Introduzca una frase >>> ")
sinEspacios = frase.replace(" ","")
listFrase = list(sinEspacios)
print(tuple(listFrase))
