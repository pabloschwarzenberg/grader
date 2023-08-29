class Vector:
    def __init__ (self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.norma=(self.x**2+self.y**2+self.z**2)**0.5
    
    def __add__(self,v2):
        if isinstance(self,Vector) and isinstance(v2,Vector):
            x=v1.x+v2.x
            y=v1.y+v2.y
            z=v1.z+v2.z
            return Vector(x,y,z)    
    
    def __repr__(self):
        return str(self.x)+"\n"+str(self.y)+"   n: "+str(self.norma)+"\n"+str(self.z)


def suma_vectores(v1,v2):
   if isinstance(v1,Vector) and isinstance(v2,Vector):
      x=v1.x+v2.x
      y=v1.y+v2.y
      z=v1.z+v2.z
      return Vector(x,y,z)
      
  