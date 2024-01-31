'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 15
##########################################
El mateix que l’anterior exercici, 
però sense demanar un màxim de números. 
L’usuari indicarà quan ha acabat 
posant un 0.
'''
tuplaNumeros = set()
i=0
valor = 2
acumulador = ','

while valor != '0':
    valor = input("Introduzca valores separados por un espacio (0 para salir) >>> ")
    acumulador = + valor.split()

print(acumulador)
numeros=acumulador.split(',') 
print(numeros)
# for numero in numeros:
#     numero = numero.strip() #eliminamos los espacios
#     tuplaNumeros.add(int(numero))


print(tuple(sorted(list(tuplaNumeros)))) #convertimos en lista para poder ordenar







