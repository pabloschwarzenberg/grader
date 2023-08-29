class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __add__(self,other):
        r=Vector(0,0,0)
        r.x=self.x+other.x
        r.y=self.y+other.y
        r.z=self.z+other.z
        return r
        
    def norma(self):
        from math import sqrt
        a=sqrt(self.x**2+self.y**2+self.z**2)
        return a
 
def suma_vectores(a,b):
    r=Vector(0,0,0)
    r.x=a.x+b.x
    r.y=a.y+b.y
    r.z=a.z+b.z
    return r