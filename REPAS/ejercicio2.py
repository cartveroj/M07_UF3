'''
WEB HÍBRIDES-M07
Veronica Cartagena
Ejercicio 2
Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que 
introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i finalment mostrar, per pantalla, 
el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.

'''

valor = int(input("Introduzca un valor "))
iva = int(input("Introduzca un porcentaje 4%, 10% o 21% "))
resultado = (iva * valor/100)+valor

print( "El valor introducido es" , valor ,"euros \nEl valor final con IVA: " , resultado)