# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("La operación de suma solo es válida entre objetos de la clase Vector")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        x = vector1.x + vector2.x
        y = vector1.y + vector2.y
        z = vector1.z + vector2.z
        return Vector(x, y, z)
    else:
        raise TypeError("La función suma_vectores solo acepta objetos de la clase Vector como parámetros")

           