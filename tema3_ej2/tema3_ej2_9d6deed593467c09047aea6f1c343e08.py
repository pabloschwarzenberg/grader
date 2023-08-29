class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def norma(self):
        return ((self.x*self.x)+(self.y*self.y)+(self.z*self.z))**(1/2)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

def suma_vectores(a, b):
    return Vector(a.x+b.x, a.y+b.y, a.z+b.z)