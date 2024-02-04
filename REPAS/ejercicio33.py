'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 33
##########################################
PROGRAMACIÓ FUNCIONAL
Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
Exemple llista compra: {100:10, 250:5, 1500:30, …}
on 100 és el preu i 20 el descompte a aplicar a aquests 100.
Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.
Exemple:
Producte 1: 
Producte 2:

'''
import ejercicio31

def calculo_descuentos(lista_compra):
    total = []
    for precio, desc in lista_compra.items():
        total.append(precio-(desc * precio/100))
    return total

lista_compra = {100:10, 250:5, 1500:30}

conDescuento = calculo_descuentos(lista_compra)
print(lista_compra)
suma = 0
index = 1
for numero in conDescuento:
  print(f"Producto {index} c/desc", numero)
  index+=1
  suma += numero

iva = int(input("Introduzca un tipo de IVA (4,10 o 21) >>> "))
listaIva = [4,10,21]

if(iva in listaIva):

    total = ejercicio31.calculo_con_iva(suma, iva)

else:
    iva= listaIva[2]
    total = ejercicio31.calculo_con_iva(suma, iva)
print(f"s/IVA total: {suma}")
print(f"IVA: {iva}\n{total}")




