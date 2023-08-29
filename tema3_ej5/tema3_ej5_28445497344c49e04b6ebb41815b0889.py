import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distancia(self,other):
        a=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return a
    def camino(self,other):
        x=self.x
        y=self.y
        lista=[[x,y]]
        while True:
            if x==other.x and y==other.y:
                return lista
            else:
                if x<other.x:
                    x+=1
                elif x>other.x:
                    x-=1
                if y<other.y:
                    y+=1
                elif y>other.y:
                    y-=1
                lista.append([x,y])


if __name__ == "__main__":
  pass
         