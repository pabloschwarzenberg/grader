__version__ = "1.0"
import math

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def __repr__(self):
        return "[{0},{1},{2}]".format(self.x,self.y,self.z)

    def __add__(self, other):
        r=Vector(0,0,0)
        r.x=self.x+other.x
        r.y=self.y+other.y
        r.z=self.z+other.z
        return r

def suma_vectores(v1,v2):
    r=Vector(0,0,0)
    r.x=v1.x+v2.x
    r.y=v1.y+v2.y
    r.z=v1.z+v2.z
    return r

if __name__ == "__main__":
    unitario=Vector(1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3))
    print(unitario.norma())

    v1=Vector(2,3,2)
    print(v1.norma())

    v2=Vector(3,2,3)
    print(suma_vectores(v1,v2))

    print(v1+v2)