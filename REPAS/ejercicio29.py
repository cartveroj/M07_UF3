'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 29
##########################################
FUNCIONS
Crear una funció que passats dos números per paràmetre (demanats a l’usuari)
ens mostra per pantalla tots els números (enters) que hi ha entre ells.
També mostrarà per pantalla la suma d’aquests números enters
'''

def numeros_entre_dos_valores(n1, n2):
    suma = 0
    lista_num = []
    for i in range(n1+1,n2):
        lista_num.append(i)
        suma +=i

    return lista_num, suma
     



