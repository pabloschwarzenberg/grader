import math

class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z

  def norma(self):
    norma=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    return norma

  def getx(self):
      return self.x

  def gety(self):
      return self.y

  def getz(self):
      return self.z

  def __add__(self, other):
      v3=Vector(self.getx()+other.getx(),self.gety()+other.gety(),self.getz()+other.getz())
      return v3

  def __str__(self):
      return "{0},{1},{2}".format(self.x,self.y,self.z)



def suma_vectores(v1,v2):
    v3=Vector(v1.getx()+v2.getx(),v1.gety()+v2.gety(),v1.getz()+v2.getz())
    return v3

v1=Vector(1,2,3)
v2=Vector(2,3,4)

print(suma_vectores(v1,v2))

           