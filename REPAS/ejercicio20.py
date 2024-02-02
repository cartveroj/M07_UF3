'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 20
##########################################
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat.
 S’haura de demanar a l’usuari que posi contactes (noms i edats). 
 Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
 Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

'''
noRepetido = False
dicPerson = {
    "veronica" : 30,
    "carlos" : 30
}

while noRepetido == False:
    nom = input("introduzca un nombre >>> ")
    edad = input("introduzca una edad >>> ")
    if( nom not in dicPerson.keys()):
        dicPerson[nom] = edad
    else:
        noRepetido = True
        print("Ya existe un registro con ese nombre")


print(dicPerson)

