class Vector:
  def _init_(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    d=(self.x)^2
    f=(self.y)^2
    e=(self.z)^2
    return((d+f+e)^(1/2))
  
  def __add__(self,other):
    r=Vector(0,0,0)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r
    
  