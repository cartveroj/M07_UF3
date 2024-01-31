'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 12
##########################################
LLISTES, TUPLES I DICCIONARIS
Crear una tupla amb els mesos de l’any. 
Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla 
el mes corresponent al número indicat per l’usuari. 
El programa finalitza només quan l’usuari posa 0.

'''
meses = ('enero','febrero','marzo','abril',
         'mayo','junio','julio','agosto','septiembre','octubre'
         ,'noviembre','diciembre')

valor = 2
while valor != 0  and valor <=12:
    valor = int(input("Introduzca un numero del 1 al 12 (0 para salir) >>> ")) 
    if valor > 0 and valor <=12:
        print(meses[valor-1])

print("bye bye")    


