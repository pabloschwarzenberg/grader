# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


    def __add__(self, other):
        i=self.x+other.x
        k=self.y+other.y
        j=self.z+other.z
        v=Vector(i,k,j)
        return v
    def norma(self):
        n= ((float(self.x))**2+(float(self.y))**2+(float(self.z))**2)**(1/2)
        return n
 

def suma_vectores(v1,v2):
  v3=v1+v2
  return v3 
           