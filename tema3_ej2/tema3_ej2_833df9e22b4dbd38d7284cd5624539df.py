class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        a=self.x*self.x
        b=self.y*self.y
        c=self.z*self.z
        d=a+b+c
        e=d**(1/2)
        return(e)
 
    def __add__(self,b):
        sumax=self.x+b.x
        sumay=self.y+b.y
        sumaz=self.z+b.z
        return Vector(sumax,sumay,sumaz)
        
def suma_vectores(v1,v2):
        a=v1.x+v2.x
        b=v1.y+v2.y
        c=v1.z+v2.z
        return Vector(a,b,c)
        
        