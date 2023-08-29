class Vector:
    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        from math import sqrt
        self.norma= sqrt(z**2+x**2+y**2)

def suma_vectores(v1,v2):
    x=v1.x+v2.x
    y=v1.y+v2.y
    z=v1.z+v2.z
    suma = Vector(x,y,z)
    return suma