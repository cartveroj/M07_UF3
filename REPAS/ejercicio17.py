'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 17
##########################################
Igual que l’anterior però a la tupla afegir la frase 
sense els caràcters repetits i mostrar el contingut de la tupla. 
Exemple: Usuari indica la paula caracteristica. 
Es mostra per pantalla carteis

'''
frase = input("Introduzca una frase >>> ")

sinEspacios = frase.replace(" ","")
sinRepetidos = set()
for i, caracter in enumerate(sinEspacios):
   for j in range(i+1, len(sinEspacios)):
      if caracter != sinEspacios[j]:
         sinRepetidos.add(caracter)

print(sinRepetidos)
