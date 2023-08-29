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
            x_suma = self.x + other.x
            y_suma = self.y + other.y
            z_suma = self.z + other.z
            return Vector(x_suma, y_suma, z_suma)
        else:
            raise ValueError("El argumento debe ser una instancia de la clase Vector")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise ValueError("Ambos argumentos deben ser instancias de la clase Vector")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = suma_vectores(v1, v2)
print("Coordenadas de v3:", v3.x, v3.y, v3.z)
print("Norma de v3:", v3.norma())

           