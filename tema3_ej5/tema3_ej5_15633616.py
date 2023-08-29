import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distancia(self,p1):
        d=math.sqrt((p1.x-self.x)**2+(self.y-p1.y)**2)
        return d
    
    def camino(self,p2):
        x=self.x
        y=self.y
        lista=[[x,y]]
        while x!=p2.x or y!=p2.y:
            if x>p2.x:
                x=x-1
            if x<p2.x:
                x=x+1
            if y>p2.y:
                y=y-1
            if y<p2.y:
                y=y+1
            lista.append([x,y])
        return lista
  
         