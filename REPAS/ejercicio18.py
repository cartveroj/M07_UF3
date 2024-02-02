'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 18
##########################################
Demanar a l’usuari posar 2 paraules. 
Afegir aquestes a una tupla i mostrar 
per pantalla quantes vegades apareix cada lletra.

'''

frase = input("Introduzca dos palabras >>> ")

sinEspacios = frase.replace(" ","")
dicLetras = {}
tupla = tuple()
#creamos un diccionario
for caracter in sinEspacios.lower():
    if caracter in dicLetras:
        dicLetras[caracter] +=1
    else:
        dicLetras[caracter] =1
#convertimos a tupla
for clave, valor in dicLetras.items():
  tupla += ((clave, valor),)

print(tupla)