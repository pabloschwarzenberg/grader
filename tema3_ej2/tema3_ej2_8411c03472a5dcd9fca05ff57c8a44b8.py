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
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Invalid operand type for +")

def suma_vectores(v1, v2):
    return v1 + v2

if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)
    c = suma_vectores(a, b)
    print(c.x, c.y, c.z)  # 5 7 9
    print(a.norma())  # 3.7416573867739413
    print(b.norma())  # 8.774964387392123

           