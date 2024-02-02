'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 21
##########################################
Demanar a l’usuari que posi 10 números separats per espais. 
Afegir aquests números a una llista. 
Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. 
Mostrar per pantalla la llista.

Exemple mostra per pantalla.
Números de l’usuari:
suma total:
mitjana:

'''

valores = input("Introduzca numeros separados por un espacio >>> ")

listNum = valores.split()
suma = 0
for i in range(len(listNum)):
    suma += int(listNum[i])
media = suma/len(listNum)

print(f"Numero de usuario son :{listNum}\nsuma total {suma}\nmedia : {media}")
