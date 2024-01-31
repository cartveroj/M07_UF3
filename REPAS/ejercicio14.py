'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 14
##########################################
Demanar a l’usuari que introdueixi 10 números 
separats per un espai. 
Al acabar, el programa els introduirà en una tupla i 
els ordenarà (major o menor, com volgueu), 
mostrant per pantalla el contingut de la tupla
'''
valor = input("Introduzca valores separados por un espacio >>> ")
tuplaNumeros = set()
i=0
numeros=valor.split() 
for numero in numeros:
    numero = numero.strip() #eliminamos los espacios
    tuplaNumeros.add(int(numero))


print(tuple(sorted(list(tuplaNumeros)))) #convertimos en lista para poder ordenar







