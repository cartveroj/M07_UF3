'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 22
##########################################
XML I JSON
Crear una funció que mostri, per consola, i guardi en un arxiu extern, 
un JSON amb una key de nom book que contindrà titel, cover, year i pages. 
Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 
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

