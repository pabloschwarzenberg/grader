# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def __add__(self,other):
    suma=Vector((self.x+other.x),(self.y+other.y),(self.z+other.z))
    return suma

  def norma(self):
    import math
    norma=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    return norma

def suma_vectores(v1,v2):
  suma=v1+v2
  return suma
  
obj_vector=Vector(2,10,15)
obj_vector_2=Vector(10,15,20)
print(obj_vector.norma())
print(obj_vector+obj_vector_2)
