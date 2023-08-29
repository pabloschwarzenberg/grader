import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

def suma_vectores(vector1, vector2):
    return vector1 + vector2

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Vector v1:", v1.x, v1.y, v1.z)
print("Vector v2:", v2.x, v2.y, v2.z)

norma_v1 = v1.norma()
norma_v2 = v2.norma()

print("Norma de v1:", norma_v1)
print("Norma de v2:", norma_v2)

v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)
