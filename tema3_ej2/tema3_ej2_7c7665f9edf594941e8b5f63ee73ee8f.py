class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return self.x - self.y

    def __add__(self, other):
        x = self.x + other.x
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return {x,y,z}
        
        
def suma_vectores(v1, v2):
    return v1 + v2

