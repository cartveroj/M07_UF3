'''
WEB HÍBRIDES-M07 - Python-Basics
Veronica Cartagena
##########################################
Ejercicio 25
##########################################
FUNCIONS
Crear un arxiu de nom vehicle.py. 
En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

'''
class vehicle:
    def __init__(self, color, modelo, year, motor, numPuertas,tipo):
      self._color = color
      self._modelo = modelo
      self._year = year
      self._motor = motor
      self._numPuertas = numPuertas
      self._tipo = tipo
    
    def get_color(self):
      return self._color
    def get_modelo(self):
      return self._modelo
    def get_year(self):
      return self._year
    def get_motor(self):
      return self._motor
    def get_numPuertas(self):
      return self._numPuertas
    def get_tipo(self):
      return self._tipo

    def set_color(self, nou_color):
      self._color = nou_color
    def set_modelo(self, nou_modelo):
      self._modelo = nou_modelo
    def set_year(self, nou_year):
      self._year = nou_year
    def set_motor(self, nou_motor):
      self._modelo = nou_motor
    def set_num_puertas(self, nou_num_puertas):
      self._numPuertas = nou_num_puertas
    def set_tipo(self, nou_tipo):
      self._tipo = nou_tipo
    
    def to_dict(self):
       return{
          "color": self._color,
          "modelo": self._modelo,
          "year": self._year,
          "motor": self._motor,
          "numPuertas": self._numPuertas,
          "tipo": self._tipo
       }
    def parts(self):
        print(f"Model: {self._color}")
        print(f"Marca: {self._modelo}")
        print(f"Matrícula: {self._year}")
        print(f"Color: {self._motor}")
        print(f"Nombre de portes: {self._numPuertas}")
        print(f"Cilindrada: {self._tipo}")


