# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
         norma=((self.x*self.x)+(self.y*self.y)+(self.z*self.z))**(1/2)
         return norma
    def __add__ (self,v2):
        a=self.x+v2.x
        b=self.y+v2.y
        c=self.z+v2.z
        return Vector(a,b,c)
    
def suma_vectores(v1,v2):
    return v1+v2

           