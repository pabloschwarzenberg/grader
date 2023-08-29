import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return norma
    def suma_vectores(self,vector_2):
        a=self.x+vector_2.x
        b=self.y+vector_2.y
        c=self.z+vector_2.z
        suma=Vector(a,b,c)
        return suma
        
    def __add__(self, otrov):
      return self.suma_vectores(otrov)
 
def suma_vectores(self,vector_2):
        a=self.x+vector_2.x
        b=self.y+vector_2.y
        c=self.z+vector_2.z
        suma=Vector(a,b,c)
        return suma
    
vector=Vector(1,2,3)
vector1=Vector(2,3,4)
x=vector.norma()
y=vector.suma_vectores(vector1)
print(x)
print(y)


           