'''
WEB HÍBRIDES-M07
Veronica Cartagena
Ejercicio 3
Demanar a l’usuari que introdueixi 2 valors i mostrar, 
per pantalla, quin és el més gran.

'''

valor1 = int(input("Introduzca un primer valor "))
valor2 = int(input("Introduzca un segungo valor "))

result = valor1 if valor1 > valor2 else valor2

print( "El mayor es" , result)