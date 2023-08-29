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
            raise TypeError("Operand must be a Vector object")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Both operands must be Vector objects")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calculando la norma del vector v1
print("Norma de v1:", v1.norma())

# Sumando dos vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

# Usando la sobrecarga del operador '+'
v4 = v1 + v2
print("Suma de v1 y v2 (usando sobrecarga de operador):", v4.x, v4.y, v4.z)
