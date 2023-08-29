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
            raise TypeError("Operands must be instances of the Vector class")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Operands must be instances of the Vector class")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

resultado = suma_vectores(v1, v2)
print(resultado.x, resultado.y, resultado.z)  # Output: 5 7 9

norma_v1 = v1.norma()
print(norma_v1)  # Output: 3.7416573867739413
           