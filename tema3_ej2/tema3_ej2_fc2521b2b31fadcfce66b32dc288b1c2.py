# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def norma(self):
        norm=self.x*self.x+self.y*self.y+self.z*self.z
        norm=math.sqrt(norm)
        return norm

    def descomponer(self):
        self.list=[self.x,self.y,self.z]
        return self.list

def suma_vectores(v1,v2):
    l1=v1.descomponer()
    l2=v2.descomponer()
    a=l1[0]+l2[0]
    b=l1[1]+l2[1]
    c=l1[2]+l2[2]
    vf=Vector(a,b,c)
    return vf
