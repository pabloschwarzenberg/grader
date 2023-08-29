# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
  def norma(self):
    norm=((self.x**2)+(self.y**2)+(self.z**2))**(0.5)
    return norm
  def __add__(self,other):
    suma_posc_x=self.x+other.x
    suma_posc_y=self.y+other.y
    suma_posc_z=self.z+other.z
    return Vector(suma_posc_x,suma_posc_y,suma_posc_z)
    
def suma_vectores(v1,v2):
    suma_de_x=v1.x+v2.x
    suma_de_y=v1.y+v2.y
    suma_de_z=v1.z+v2.z
    final=Vector(suma_de_x,suma_de_y,suma_de_z)
    return final
           