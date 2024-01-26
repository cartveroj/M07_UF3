'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 8
##########################################
Demanar a l’usuari que posi entre 1 i 3 paraules. 
Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari,
indicar quants caràcters té i indicar el primer, i l’últim caràcter.

'''
input = input("Introduzca entre 1 a 3 palabras-> ")
palabras = input.split(" ")
numeroPalabras = len(palabras)

for palabra in palabras :
    print("la palabra:", palabra ,"longitud:",len(palabra))
    print("primer caracter:",palabra[0])
    print("ultimo caracter:",palabra[-1])





