'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 23
##########################################
XML I JSON
Crear una funció que mostri, per consola, i guardi en un arxiu extern, 
un JSON amb una key de nom book que contindrà titel, cover, year i pages. 
Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 
'''
import json


def book(titulo, tapa, año, paginas):
  """Crea un diccionario con la información de un libro."""
  return {
    "titulo": titulo,
    "tapa": tapa,
    "year": año,
    "paginas": paginas
  }
books = [
    book("El gato con botas","dura","1980","180"),
    book("señor de los anillos","dura","1980","280"),
    book("patito feo","blanda","1980","180"),
    book("Biblia","dura","1980","450"),
]
books_list = []
for book in books:
    books_list.append(book)

clave="book" #creamos la clave
     

dataJson = {clave:books} #creamos el diccionario
print(json.dumps(dataJson))

with open("books.json", 'w') as file: #creamos el archivo externo
   json.dump(dataJson, file, indent=4)


# crear_json_books() #llamamos a la funcion
   
def to_dict(self):
    return{
        "title":self.title,
        "cover":self.cover,
        "year":self.year,
        "pages":self.pages,
    }
