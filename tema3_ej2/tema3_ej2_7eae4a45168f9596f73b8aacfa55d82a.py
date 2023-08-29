import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __repr__(self):
        return print("Vector", self.x, self.y, self.z)

def suma_vectores(a, b):
    return a + b

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print("Norma de v1:", v1.norma())
    print("Norma de v2:", v2.norma())
    
    v3 = suma_vectores(v1, v2)
    print("Suma de v1 y v2:", v3)
