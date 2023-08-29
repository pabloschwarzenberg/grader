class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=(self.x**2+self.y**2+self.z**2)**(1/2)
        return norma
        
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)

    def __str__(self):
        return "{0} {1} {2}".format(self.x,self.y,self.z)
        
def suma_vectores(v1,v2):
  return v1+v2
        
if __name__ == "__main__":      
  x=int(input("x"))
  y=int(input("Y"))
  z=int(input("Z"))
  vector1=Vector(x,y,z)
  print(vector1.norma())
  vector2=Vector(1,2,1)
  