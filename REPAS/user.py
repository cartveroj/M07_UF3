'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 26
##########################################
FUNCIONS
Crear un arxiu de nom user.py. 
En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json


'''
class user:
    def __init__(self, name, surname,age, dni, email,phone):
      self._name = name
      self._surname = surname
      self._age = age
      self._dni = dni
      self._email = email
      self._phone = phone
    
    def get_name(self):
      return self._name
    def get_surname(self):
      return self._surname
    def get_age(self):
      return self._age
    def get_dni(self):
      return self._dni
    def get_email(self):
      return self._email
    def get_phone(self):
      return self._phone

    def set_name(self, nou_name):
      self._name = nou_name
    def set_surname(self, nou_surname):
      self._surname = nou_surname
    def set_age(self, nou_age):
      self._age = nou_age
    def set_dni(self, nou_dni):
      self._surname = nou_dni
    def set_num_puertas(self, nou_num_puertas):
      self._email = nou_num_puertas
    def set_phone(self, nou_phone):
      self._phone = nou_phone
    
    def to_dict(self):
       return{
          "name": self._name,
          "surname": self._surname,
          "age": self._age,
          "dni": self._dni,
          "email": self._email,
          "phone": self._phone
       }
    
    def salutacio(self):
        print(f"My name is: {self._name}")
        print(f"My surname is: {self._surname}")
        print(f"My age is: {self._age}")
        print(f"My dni is: {self._dni}")
        print(f"My email is: {self._email}")
        print(f"My phone number is: {self._phone}")


