import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("La operación de suma solo es válida entre objetos de la clase Vector")

def suma_vectores(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        return a + b
    else:
        raise TypeError("La operación de suma solo es válida entre objetos de la clase Vector")
