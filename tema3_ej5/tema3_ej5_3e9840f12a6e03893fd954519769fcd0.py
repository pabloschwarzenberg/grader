import math

class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        lista=[]
        lista.append(x)
        lista.append(y)
        
    def camino(self,otro):
        dx=self.x-otro.x
        dy=self.y-otro.y
        x=math.sqrt((dx)**2+(dy**2))
        return x
         