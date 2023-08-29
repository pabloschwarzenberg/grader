from math import sqrt
class Vector():
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.suma_vectores=[]
        suma_vectores=self.suma_vectores
         
     
    def norma(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
 
    def __add__(self,other):
        n=Vector(0,0,0)
        n.x=(self.x+other.x)
        n.y=(self.y+other.y)
        n.z=(self.z+other.z)
        self.suma_vectores.append(n)
        return n
       
        
    def __repr__(self):
        
        return "{0} {1} {2}".format(self.x,self.y,self.z)
        