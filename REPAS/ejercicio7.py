'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
Ejercicio 7
LOOPS: Mostrar els números imparells de l’1 al 500.

'''
numero = 0
while numero < 500:
    numero+=1
    result = numero if numero % 2 == 1 else ''
    print( result )
