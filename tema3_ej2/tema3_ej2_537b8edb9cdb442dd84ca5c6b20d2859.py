import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.componentes=[x,y,z]
    def norma(self):
        a=self.x*self.x
        b=self.y*self.y
        c=self.z*self.z
        d=a+b+c

        e=math.sqrt(d)
        return e
    def __repr__(self):
        s=""
        for i in range(len(self.componentes)):
            s=s+"{0:<8.2f}".format(self.componentes[i])
        return s
    def __add__(self,otro):
        xf=self.x+otro.x
        yf=self.y+otro.y
        zf=self.z+otro.z
        return Vector(xf,yf,zf)
    
def suma_vectores(v1,v2):
    xf=v1.x+v2.x
    yf=v1.y+v2.y
    zf=v1.z+v2.z
    vf=Vector(xf,yf,zf)
    return vf
