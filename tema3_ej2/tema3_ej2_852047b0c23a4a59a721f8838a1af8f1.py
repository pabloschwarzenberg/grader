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
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise ValueError("El objeto pasado no es de tipo Vector")

def suma_vectores(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        x = a.x + b.x
        y = a.y + b.y
        z = a.z + b.z
        return Vector(x, y, z)
    else:
        raise ValueError("Los objetos pasados no son de tipo Vector")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calcular la norma del vector v1
print("Norma de v1:", v1.norma())

# Sumar dos vectores usando el método suma_vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

# Sumar dos vectores usando el operador +
v4 = v1 + v2
print("Suma de v1 y v2 (usando el operador +):", v4.x, v4.y, v4.z)
