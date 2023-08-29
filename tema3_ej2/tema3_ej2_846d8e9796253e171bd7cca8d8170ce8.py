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
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Unsupported operand type for +")

def suma_vectores(v1, v2):
    return v1 + v2

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)  # Resultado: 5, 7, 9

norma_v1 = v1.norma()
print(norma_v1)  # Resultado: 3.7416573867739413
