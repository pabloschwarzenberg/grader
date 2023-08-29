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
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Operación no válida. El operando debe ser un objeto de la clase Vector.")

def suma_vectores(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        return a + b
    else:
        raise TypeError("Operación no válida. Los operandos deben ser objetos de la clase Vector.")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Cálculo de la norma de v1
norma_v1 = v1.norma()
print("Norma de v1:", norma_v1)

# Suma de v1 y v2 usando el método suma_vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

# Suma de v1 y v2 usando la sobrecarga del operador '+'
v4 = v1 + v2
print("Suma de v1 y v2 (con sobrecarga de operador):", v4.x, v4.y, v4.z)
