# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.l=[]
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        return math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
    def __str__(self):
        return ("el vector es ("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")")
    
    def __add__(self,other):
        self.a=other.x
        self.b=other.y
        self.c=other.z
        return Vector(self.a+self.x,self.b+self.y,self.c+self.z)
def suma_vectores(a,b):
    v1=a.x
    v2=a.y
    v3=a.z
    u1=b.x
    u2=b.y
    u3=b.z
    return Vector(v1+u1,v2+u2,v3+u3)