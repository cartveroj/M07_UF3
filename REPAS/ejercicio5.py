'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
Ejercicio 5
Demanar a l’usuari un número. Indicar si el número 
inserit per l’usuari és parell o senar.

'''

valor = int(input("Introduzca un primer valor "))
par = "es Par"
impar = "es impar"
result = par if valor%2 == 0 else impar

print( "El valor introducido", valor, result)