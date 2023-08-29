class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        norma = (self.x**2+self.y**2 +self.z**2)**(1/2)
        return norma

    def __add__(self, v1):
        r=Vector(0,0,0)
        r.x = self.x + v1.x
        r.y = self.y + v1.y
        r.z = self.z + v1.z
        return r
        
def suma_vectores(v1, v2):
    contadorx=0
    contadory=0
    contadorz=0
    return Vector(v1.x+v2.x,v1.y + v2.y,v1.z + v2.z)