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
            raise TypeError("El objeto debe ser de tipo Vector")
            

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        x_sum = vector1.x + vector2.x
        y_sum = vector1.y + vector2.y
        z_sum = vector1.z + vector2.z
        return Vector(x_sum, y_sum, z_sum)
    else:
        raise TypeError("Los objetos deben ser de tipo Vector")


# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calcula la norma del vector v1
norma_v1 = v1.norma()
print("Norma del vector v1:", norma_v1)

# Suma dos vectores utilizando el método suma_vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

# Suma dos vectores utilizando el operador +
v4 = v1 + v2
print("Suma de v1 y v2:", v4.x, v4.y, v4.z)
