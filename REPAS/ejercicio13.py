'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 13
##########################################
LLISTES, TUPLES I DICCIONARIS
Demanar a l’usuari un número de l’1 al 10 i mostrar 
per pantalla la seva taula de multiplicar fins el 10. 
Exemple: l’usuari marca 3, es mostra per 
pantalla: 3,6,9,12,15,18,21,24,27 i 30
'''
valor = int(input("Introduzca un numero del 1 al 10 >>> ")) 
if valor <= 10 and valor > 0:
    numeros = set()
    for i in range(1, 11):
        numeros.add(valor * i)

    print(tuple(sorted(list(numeros))))
else:
    print("fuera de rango")





