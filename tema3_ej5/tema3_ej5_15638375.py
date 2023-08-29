class Ciudad():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,c):
        a=self.x
        b=self.y
        camino=[[a,b]]
        while a!=c.x or b!=c.y:
            if a<c.x and b<c.y:
                camino.append([a+1,b+1])
                a=a+1
                b=b+1
            elif a==c.x and b<c.y:
                camino.append([a,b+1])
                b=b+1
            elif a>c.x and b<c.y:
                camino.append([a-1,b+1])
                a=a-1
                b=b+1
            elif a<c.x and b==c.y:
                camino.append([a+1,b])
                a=a+1
            elif a<c.x and b>c.y:
                camino.append([a+1,b-1])
                a=a+1
                b=b-1
            elif a>c.x and b>c.y:
                camino.append([a-1,b-1])
                a=a-1
                b=b-1
        return camino
    def distancia(self, c):
        dist=((self.x-c.x)**2+(self.y-c.y)**2)**(1/2)
        return dist
        

if __name__ == "__main__":
  pass
         