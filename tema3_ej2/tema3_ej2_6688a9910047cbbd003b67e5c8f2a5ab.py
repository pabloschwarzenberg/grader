# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.vector_ordenado = [[x],[y],[z]]
    def norma(self):
        norma = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return norma
    def __add__(self,other):
        if isinstance(self,Vector) and isinstance(other,Vector):
            suma_x = self.x + other.x
            suma_y = self.y + other.y
            suma_z = self.z + other.z
            suma_vector = Vector(suma_x,suma_y,suma_z)
            return suma_vector
            
def suma_vectores(a,b):
    if isinstance(a,Vector) and isinstance(b,Vector):
        suma_x = a.x + b.x
        suma_y = a.y + b.y
        suma_z = a.z + b.z
        suma_vector = Vector(suma_x,suma_y,suma_z)
        return suma_vector
           