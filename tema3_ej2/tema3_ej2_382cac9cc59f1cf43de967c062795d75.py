#crear clase vector y mÃ©todo de mÃ³dulo y mÃ©todo de suma para la clase
from math import sqrt
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        cuadrado_abscisa = self.x**2
        cuadrado_ordenada = self.y**2
        cuadrado_azimutal = self.z**2
        suma_de_los_cuadrados = cuadrado_abscisa + cuadrado_ordenada + cuadrado_azimutal
        modulo = sqrt(suma_de_los_cuadrados)
        return modulo

    def __add__(self, other):
        #faltaba llamar al constructor de la clase Vector
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

#suma vectores debe ser una función que reciba objetos de la clase Vector
def suma_vectores(self,other):
  suma_abscisa = self.x + other.x
  suma_ordenada = self.y + other.y
  suma_azimutal = self.z + other.z
  return Vector(suma_abscisa,suma_ordenada,suma_azimutal)
