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
            return NotImplemented

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        return None
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

norma_vector1 = vector1.norma()
print("Norma del vector1:", norma_vector1)

suma = suma_vectores(vector1, vector2)
if suma is not None:
    print("Suma de los vectores:", suma.x, suma.y, suma.z)
else:
    print("No se puede sumar los vectores.")
