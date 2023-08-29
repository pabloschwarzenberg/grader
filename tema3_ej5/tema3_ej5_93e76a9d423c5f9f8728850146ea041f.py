import math

class Ciudad:
  def __init__(self,x,y):
      self.x=x
      self.y=y
  def camino(self,other):
      mediox=(self.x + other.x)/2
      medioy=(self.y + other.y)/2
      lista=[[self.x,self.y],[mediox,medioy],[other.x,other.y]]
      return lista
 
  def distancia(self,other):
      distancia=math.sqrt((self.x-other.x)*2 + (self.y-other.y)*2)
      return distancia

if _name_ == "_main_":
  pass