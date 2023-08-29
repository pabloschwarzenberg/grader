class Vector:
      def __init__(self,x,y,z):
          self.x = x
          self.y = y
          self.z = z
      
      def norma(self):
          norma = ((float(self.x))**2 + (float(self.y))**2 + (float(self.z)**2))**(1/2)
          return norma
      
      def __add__(self,other):
          return ("{},{},{}".format(self.x+other.x,self.y+other.y,self.z+other.z))


           