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
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Operandos inválidos. Se requiere un objeto de la clase Vector.")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Operandos inválidos. Se requieren objetos de la clase Vector.")

# Crear objetos de la clase Vector
v1 = Vector(2, 3, 4)
v2 = Vector(1, -1, 2)

# Calcular la norma de v1
norma_v1 = v1.norma()
print("Norma de v1:", norma_v1)

# Sumar v1 y v2 utilizando la función suma_vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

# Sumar v1 y v2 utilizando la sobrecarga del operador '+'
v4 = v1 + v2
print("Suma de v1 y v2 (sobrecarga de operador):", v4.x, v4.y, v4.z)