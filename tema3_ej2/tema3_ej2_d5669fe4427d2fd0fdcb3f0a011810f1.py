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
            raise TypeError("La operación de suma solo es válida entre dos objetos de la clase Vector")
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Los parámetros deben ser objetos de la clase Vector")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Norma del vector v1:", v1.norma())
print("Norma del vector v2:", v2.norma())

v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3)

v4 = v1 + v2
print("Suma de v1 y v2 (usando sobrecarga de operadores):", v4)

