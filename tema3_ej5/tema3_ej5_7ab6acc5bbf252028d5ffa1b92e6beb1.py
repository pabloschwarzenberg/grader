class Ciudad:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pasos=[]

    def distancia(self,other):
        import math
        distancia = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distancia
    def camino(self,other):
        a = [self.x, self.y]
        self.pasos.append(a)
        x=self.x
        y=self.y
        if x!=other.x and y!=other.y:
            while x!=other.x and y!=other.y:
                if x<other.x:
                    x+=1
                else:
                    x-=1
                if y<other.y:
                    y+=1
                else:
                    y-=1
                a=[x,y]
                self.pasos.append(a)
        if x!=other.x:
            while x != other.x :
                if x < other.x:
                    x += 1
                else:
                    x -= 1
                a=[x,y]
                self.pasos.append(a)
        if y!=other.y:
            while y != other.y :
                if y < other.y:
                    y += 1
                else:
                    y -= 1
                a = [x, y]
                self.pasos.append(a)
        return self.pasos
    def __str__(self):
        return

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.camino(p2))
    print(p1.distancia(p2))
    
