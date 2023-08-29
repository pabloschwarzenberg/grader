import math
class Ciudad:
    def __init__(self,x,y):
        self.x=int(x)
        self.y=int(y)
        
    def camino(self,other):
        camino=[[self.x,self.y]]
        x=self.x
        y=self.y
        while x!=other.x and y!=other.y:
            if x<other.x and y<other.y:
                x+=1
                y+=1
            elif x>other.x and y>other.y:
                x-=1
                y-=1
            elif x<other.x:
                x+=1
            elif x>other.x:
                x-=1
            elif y<other.y:
                y+=1
            elif y>other.y:
                y-=1
            camino.append([x,y])
        return camino
        
    def distancia(self,other):
        d=math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        return d
    pass

if __name__ == "__main__":
  pass
         