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
# acumulador = " "
# valor = 2

# while valor != '0':
#     valor = input("Introduzca valores separados por un espacio (0 para salir) >>> ")
#     acumulador =  valor.replace(" ",",")+ ","+acumulador #acumulamos los valores


# lista = acumulador.strip().split(",") #convertimos en lista
# for i in lista:
#   if i == '' or i == '0':
#     lista.remove(i) #removemos vacios y el 0 


# print(tuple(sorted(lista))) #ordenamos y printamos

'''
Ejercicio 16
##########################################
Demanar a l’usuari una frase. 
El programa eliminarà els espais i s'afegirà a una tupla. 
Mostrar per pantalla el contingut de la tupla.

'''

# frase = input("Introduzca una frase >>> ")
# sinEspacios = frase.replace(" ","")
# listFrase = list(sinEspacios)
# print(tuple(listFrase))

'''
Ejercicio 17
##########################################
Igual que l’anterior però a la tupla afegir la frase 
sense els caràcters repetits i mostrar el contingut de la tupla. 
Exemple: Usuari indica la paula caracteristica. 
Es mostra per pantalla carteis

'''
# frase = input("Introduzca una frase >>> ")

# sinEspacios = frase.replace(" ","")
# sinRepetidos = set()
# for i, caracter in enumerate(sinEspacios):
#    for j in range(i+1, len(sinEspacios)):
#       if caracter != sinEspacios[j]:
#          sinRepetidos.add(caracter)

# print(sinRepetidos)

'''
Ejercicio 18
##########################################
Demanar a l’usuari posar 2 paraules. 
Afegir aquestes a una tupla i mostrar 
per pantalla quantes vegades apareix cada lletra.

'''

# frase = input("Introduzca dos palabras >>> ")

# sinEspacios = frase.replace(" ","")
# dicLetras = {}
# tupla = tuple()
# #creamos un diccionario
# for caracter in sinEspacios.lower():
#     if caracter in dicLetras:
#         dicLetras[caracter] +=1
#     else:
#         dicLetras[caracter] =1
# #convertimos a tupla
# for clave, valor in dicLetras.items():
#   tupla += ((clave, valor),)

# print(tupla)

'''
Ejercicio 19
##########################################
Cal buscar la informació que es demana de la següent list:
areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34,
 “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)
Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
Imprimir el total de l’àrea del pis.


'''
areas_pis = ['Menjador', 10.15, 
             'Rebedor', 9.56,
             'Habitació', 12.34,
            'Terrassa', 15.55, 
            'Lavabo', 7.98, 
            'Cuina', 12, 
            'Habitació2', 12.23]
# Imprimir el segon element
print(areas_pis[1])
# Imprimir l’últim element
print(areas_pis[-1])
# Imprimir l’àrea de la terrassa
print(areas_pis[6],areas_pis[7])
# Imprimir del primer element al tercer element
print(areas_pis[0:4])
# Imprimir del tercer element a l’últim
print(areas_pis[4:])
# Imprimir el total de l'àrea de les dues habitacions
suma=0
for i in range(len(areas_pis)):
    if areas_pis[i] == 'Habitació':
        suma += areas_pis[i+1]

    elif  areas_pis[i] == 'Habitació2':
        suma += areas_pis[i+1]

print(suma)
# Modificar l’àrea del lavabo i imprimir la nova list area
areas_pis.insert(9,10)
print(areas_pis)
# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
data = ('pati interior' , 2.78)
areas_pis.extend(data)
print(areas_pis)
# Imprimir el total de l’àrea del pis.
val1=0
val2=0
for i in range(len(areas_pis)):
    if type(areas_pis[i]) == float :
        val1 += areas_pis[i]
    elif type(areas_pis[i])  == int:
        val2 += areas_pis[i]

print(val1+val2)

'''
Ejercicio 20
##########################################
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat.
 S’haura de demanar a l’usuari que posi contactes (noms i edats). 
 Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
 Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

'''
