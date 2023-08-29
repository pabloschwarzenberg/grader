class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        norm = (self.x**2 + self.y**2 + self.z**2)**(1/2)
        return norm

    def __add__(self, v):
        vx = (self.x + v.x)
        vy = (self.y + v.y)
        vz = (self.z + v.z)
        vsum = Vector(vx, vy, vz)
        return vsum

def suma_vectores(v1,v2):
    vx = v1.x + v2.x
    vy = v1.y + v2.y
    vz = v1.z + v2.z
    v = Vector(vx, vy, vz)
    return v