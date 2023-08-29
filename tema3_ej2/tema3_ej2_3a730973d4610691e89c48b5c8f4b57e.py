# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:

    def __init__(self,x,y,z):
       self.x=x
       self.y=y
       self.z=z
   
    def norma(self):
       calculo=(self.x**2+self.y**2+self.z**2)**(1/2)
       return calculo
    
    def __add__(self,other):
        sumax = self.x + other.x
        sumay = self.y + other.y
        sumaz = self.z + other.z
        vectorsuma1 = Vector(sumax, sumay, sumaz)
        return vectorsuma1

def suma_vectores(v1,v2):
    sumax = v1.x + v2.x
    sumay = v1.y + v2.y
    sumaz = v1.z + v2.z
    vectorsuma1 = Vector(sumax, sumay, sumaz)
    return vectorsuma1
    
  
       
           