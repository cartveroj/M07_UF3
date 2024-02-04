'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 24
##########################################
XML I JSON
Crear una funció que llegeixi el JSON de l’exercici anterior 
i surti el resultat (en format json) per consola. 
'''
import json

def lectura_archivos_json():
 
   with open("books.json", 'r') as file: #creamos el archivo externo
     result = json.load(file)
     print(result)

lectura_archivos_json()


