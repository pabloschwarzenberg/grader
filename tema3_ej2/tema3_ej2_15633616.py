import math
class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        n=math.sqrt(float(self.x)**2+float(self.y)**2+float(self.z)**2)
        return n
    def __add__(self,v2):
        v3=Vector(self.x+v2.x, self.y+v2.y, self.z+v2.z)
        return v3
def suma_vectores(v1,v2):
    v1=Vector(v1.x,v1.y,v1.z)
    v2=Vector(v2.x,v2.y,v2.z)
    v3=Vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)
    return v3