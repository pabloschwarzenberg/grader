from math import sqrt
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=sqrt(self.x**2+self.y**2+self.z**2)
        return(norma)
    def __add__(self,vector2):
        r=Vector()
        r.x=self.x+vector2.x
        r.y=self.y+vector2.y
        r.z=self.z+vector2.z
        return(r)
def suma_vectores(v1,v2):
    r=Vector()
    r.x=v1.x + v2.x
    r.y=v1.y + v2.y
    r.z=v1.z + v2.z
    return(r)

           