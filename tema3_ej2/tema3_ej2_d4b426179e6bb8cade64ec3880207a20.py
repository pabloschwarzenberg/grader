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
            raise TypeError("Se requiere un objeto de la clase Vector para la suma.")

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Se requieren objetos de la clase Vector para la suma.")


# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Cálculo de la norma del vector v1
norma_v1 = v1.norma()
print(f"Norma de v1: {norma_v1}")

# Suma de dos vectores v1 y v2
v_suma = suma_vectores(v1, v2)
print(f"Suma de v1 y v2: {v_suma}")

# Uso del operador +
v3 = v1 + v2
print(f"v1 + v2 = {v3}")