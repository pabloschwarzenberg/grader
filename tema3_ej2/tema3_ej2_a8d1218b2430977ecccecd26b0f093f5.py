# crea la clase Vector y completa el código de la función suma_vectores usándola
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
            return

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        return

if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)

    print(a.norma()) 
    print(b.norma()) 

    c = suma_vectores(a, b)
    print(c.x, c.y, c.z)  # 5, 7, 9
      