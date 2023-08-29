class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)
    
    def __add__(self, other):
        return suma_vectores(self, other)

def suma_vectores(v1,v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z) 