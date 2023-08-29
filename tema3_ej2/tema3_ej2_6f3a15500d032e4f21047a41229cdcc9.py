# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

def suma_vectores(v1, v2):
    return v1 + v2
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)

v4 = v1 + v2
print(v4.x, v4.y, v4.z)

print(v1.norma())
print(v2.norma())
           