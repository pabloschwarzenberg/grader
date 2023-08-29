class Vector:
    def __init__(self,coordenada_x,coordenada_y,coordenada_z):
        self.x = coordenada_x
        self.y = coordenada_y
        self.z = coordenada_z

    def norma(self):
        norma = (self.x**2 + self.y**2 + self.z**2)**(1/2)
        return norma


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

def suma_vectores(v1, v2):
    x = v1.x + v2.x
    y = v1.y + v2.y
    z = v1.z + v2.z
    return Vector(x, y, z)