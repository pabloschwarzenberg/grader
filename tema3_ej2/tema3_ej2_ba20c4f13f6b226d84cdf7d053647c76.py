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
            raise TypeError("Operand must be of type Vector.")

# Función para sumar dos vectores
def suma_vectores(v1, v2):
    return v1 + v2

# Crear objetos de la clase Vector
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calcular la norma de un vector
norma_v1 = v1.norma()
print("Norma de v1:", norma_v1)

# Sumar dos vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)
