class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return  Vector(x,y,z)

    def norma(self):
        norma = (self.x**2 +
                 self.y**2 +
                 self.z**2)**0.5
        return norma

def suma_vectores(v1:Vector, v2:Vector):
    c = v1 + v2
    return c

           