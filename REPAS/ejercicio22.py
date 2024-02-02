'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 22
##########################################
XML I JSON
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML).
La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
Un root de nom students.
Cinc childs (del root) amb nom student.
Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
El text de cada etiqueta serà de la vostra elecció.
'''
import xml.etree.cElementTree as ET

root = ET.Element("students")

for x in range(5):
    student= ET.Element("student")
    student.attrib["id"] = f"{x}"
    name = ET.SubElement(student,"name")
    name.text= f"Veronica{x}"
    surname = ET.SubElement(student,"surname")
    surname.text = f"Cartagena{x}"
    email = ET.SubElement(student,"email")
    email.text= f"{x}@gmail.com"
    dni = ET.SubElement(student,"dni")
    dni.text= f"Y497640{x}W"

    root.append(student)


arbol = ET.ElementTree(root)
arbol.write("students.xml")
ET.dump(arbol)

