# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        else:
            raise TypeError("Operandos inválidos para la operación +. Se requiere un objeto de la clase Vector.")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Operandos inválidos para la suma de vectores. Se requieren objetos de la clase Vector.")

# Ejemplo de uso
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("Norma de v1:", v1.norma())
print("Norma de v2:", v2.norma())

v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y)

v4 = v1 + v2
print("Suma de v1 y v2 (usando sobrecarga de operadores):", v4.x, v4.y)
