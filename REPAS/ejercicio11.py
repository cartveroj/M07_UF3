'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 11
##########################################
LLISTES, TUPLES I DICCIONARIS
Demanar a l’usuari un nùmero entre 10 i 100.
Posar els números a una tupla desde 1 fins al número 
indicat per l’usuari.
Exemple: usuari indica 34, es crea una tupla i es mostra 
per pantalla els números de l’1 al 34 (imprimint la tupla).
'''

valor = int(input("Introduzca un numero entre 10 y 100 >>> "))
if valor >= 10 and valor <= 100 :
    myTupla = tuple(range(1, valor+1))
    print(myTupla)     
else: 
     print("El valor es erroneo")
    

