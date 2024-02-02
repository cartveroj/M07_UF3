'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
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

