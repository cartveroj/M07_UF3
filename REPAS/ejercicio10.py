'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 10
##########################################
Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. 
Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més 
gran fins que encerti i el missatge haurà d’indicar que ha encertat. 
Indicar també el número d’intents.
'''
import random

data = 2
numeroAdivinar = random.randint(1,100)
intentos = 0
gano = False
print(numeroAdivinar)
print("Numero de intentos 5 y para salir introduzca -1")
while data > 0 and intentos < 5 and data != numeroAdivinar:
    data = int(input("Introduzca un numero -> "))
    intentos +=1
    if data < (numeroAdivinar/2) and data != numeroAdivinar and data > 0:
        print("es mas grande")
    elif data < numeroAdivinar and data != numeroAdivinar and data > 0:
        print("es mas grande")
    elif data > numeroAdivinar and data != numeroAdivinar and data > 0:
        print("es mas pequeño")
      
if data == numeroAdivinar:
    print("Adivinaste..¡¡ \nNumero intentos: ", intentos)
else: 
     print("Perdiste..¡¡ \nNumero intentos: ", intentos)
    

