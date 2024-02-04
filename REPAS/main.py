'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 27, 28, 29, 30, 31 y 32
##########################################
FUNCIONS
'''
import random

import ejercicio27
import ejercicio28
import ejercicio29
import ejercicio30
import ejercicio31
import ejercicio32
'''
EJERCICIO 27 : Crear una funció que sumi dos números passats per paràmetre.
Aquests números seran demanats a l’usuari. 
(En aquest cas haurieu de tindre un arxiu on feu el càlcul de dos números 
passats per paràmetre i un arxiu main.py 
on trucarà aquesta funció i li passarà els números indicats per l’usuari.)
'''
print("Ejercicio:27")
data1 = int(input("introduzca el primer valor >>> "))
data2 = int(input("introduzca el segundo valor >>> "))

result = ejercicio27.sumaNumeros(data1, data2)
print("La suma es: ",result)

''' EJERCICIO 28 : Crear una funció que passats dos números per paràmetre
(demanats a l’usuari) ens mostri per pantalla 
un número aleatori entre aquests dos números.'''
print("Ejercicio:28")
random = ejercicio28.randomNumeros(data1, data2)
print(f"Un numero random entre {data1} y {data2} es: ",random)

'''
EJERCICIO 29 :Crear una funció que passats dos números per paràmetre (demanats a l’usuari)
ens mostra per pantalla tots els números (enters) que hi ha entre ells.
També mostrarà per pantalla la suma d’aquests números enters
'''
print("Ejercicio:29")
if(data1 < data2):
    numeros , suma = ejercicio29.numeros_entre_dos_valores(data1, data2)
    print(f"Los numeros entre {data1} y {data2} son: ", numeros)
    print(f"La suma de todos ellos es: {suma}")
else:
    print(f"el primer valor debe ser menor al segundo valor")

'''
EJERCICIO 30 :Crear una funció que passat un nom per l’usuari (nom).
Mostri per pantalla “Hola nom”.
'''
print("Ejercicio:30")
nombre = input("Introduzca un nombre >>> ")

saludo = ejercicio30.hola_mundo(nombre)
print(saludo)

'''
EJERCICIO 31 :Crear una funció per calcular el total d’una factura amb l’IVA.
La funció ha de rebre (per paràmetre) la quantitat sense IVA i l’IVA a aplicar(introduïts per l’usuari).
En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%)
s’aplicarà directament el 21%.
Es mostra per pantalla el valor sense IVA, l’IVA i el total.
'''
print("Ejercicio:31")
importe = input("Introduzca un importe >>> ")
iva = int(input("Introduzca un tipo de IVA (4,10 o 21) >>> "))
listaIva = [4,10,21]
valor = int(importe) if type(importe) == int else float(importe)
print(iva in listaIva)
if type(valor) is int or type(valor) is float:

    if(iva in listaIva):
        
        total = ejercicio31.calculo_con_iva(valor, iva)
    else:
        iva= listaIva[2]
        total = ejercicio31.calculo_con_iva(valor, iva)

    print(f"Calculo de Factura: \nImporte: {valor}\nIVA: {iva}\n{total}")
  
else:
      print("Los valores deber ser enteros o decimal")
    
'''
EJERCICIO 32 :Crear una funció que agafi una llista amb 10 números,
 i retorni una altra llista amb els seus quadrats.

'''
lista_numeros = []
for i in range(10):
    numero = random.randint(1,20)
    lista_numeros.append(numero)

cuadrados = ejercicio32.calculo_cuadrados(lista_numeros)
print("Ejercicio:32")
print(f"Llista original: {lista_numeros}")
print(f"Llista de quadrats: {cuadrados}")