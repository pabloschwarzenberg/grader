# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    def norma(self):
        import math
        norma=math.sqrt((self.x)*(self.x)+(self.y)*(self.y)+(self.z)*(self.z))
        return norma 
    def __add__(self,v):
        sumax=self.x+v.x
        sumay=self.y+v.y
        sumaz=self.z+v.z
        suma=Vector(sumax,sumay,sumaz)
        return suma
        
def suma_vectores(self,v):
    sumax=self.x+v.x
    sumay=self.y+v.y
    sumaz=self.z+v.z
    suma=Vector(sumax,sumay,sumaz)
    return suma
   
        