import math
class Ciudad:
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)

   
        
    def camino(self,other):
        a=[self.x,self.y]
        b=[other.x,other.y]
        c=[(self.x-other.x),(self.y-other.x)]
        lista=[a,c,b]
        return lista
        
       

    def distancia(self,other):
        distancia=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return distancia
        
      

if __name__ == "__main__":
  pass
         