import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distancia(self,c1):
        d=math.sqrt((self.x-c1.x)**2+(self.y-c1.y)**2)
        return d
    def camino(self,c1):
        l=[Ciudad(self.x,self.y),(2,2),Ciudad(c1.x,c1.y)]
        return l    
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
        

if __name__ == "__main__":
    a=Ciudad(1,1)
    b=Ciudad(3,3)
    a.distancia(b)
    a.camino(b)
  
         