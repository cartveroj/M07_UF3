'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 31
##########################################
FUNCIONS
Crear una funció per calcular el total d’una factura amb l’IVA.
La funció ha de rebre (per paràmetre) la quantitat sense IVA i l’IVA a aplicar(introduïts per l’usuari).
En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%)
s’aplicarà directament el 21%.
Es mostra per pantalla el valor sense IVA, l’IVA i el total.
'''

def calculo_con_iva(importe, iva):
    total = (iva*importe/100)+importe
    return f"Importe total: {round(total,2)}"
     



