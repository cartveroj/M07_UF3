'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 9
##########################################
Demanar a l’usuari que posi dues paraules. 
Al executar el programa, mostrarà per pantalla les dues paraules 
amb els dos primers caràcters de cada paraula intercanviats. 
Exemple: Quatre Camins passaria a Caatre Qumins.
'''
input = input("Introduzca dos palabras-> ")
palabras = input.split(" ")

palabra1 = palabras[0].replace(palabras[0][0:2],palabras[1][0:2])
palabra2 = palabras[1].replace(palabras[1][0:2],palabras[0][0:2])
print("Las palabras", input, "mutadas -> ", palabra1, palabra2)



