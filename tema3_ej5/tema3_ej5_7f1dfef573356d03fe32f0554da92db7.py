class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def camino(self,p2):
        g = []
        if self.x == p2.x:
            if self.y < p2.y:
                for i in range(p2.y-self.y):
                    g.append([self.x,i+self.y])
            elif self.y > p2.y:
                for i in range(self.y-p2.y):
                    g.append([self.x,self.y-i])
            g.append([p2.x,p2.y])
        elif self.y == p2.y :
            if self.x < p2.x:
                for i in range(p2.x-self.x):
                    g.append([i+self.x,self.y])
            elif self.x > p2.x:
                for i in range(self.x-p2.x):
                    g.append([self.x-i,self.y])
            g.append([p2.x,p2.y])
        elif self.x == self.y and p2.x == p2.y:
            if self.x < p2.x:
                for i in range(p2.x-self.x):
                    g.append([self.x + i,self.y+i])
                g.append([p2.x,p2.y])
            else:
                for i in range(self.x-p2.x):
                    g.append([self.x - i,self.y-i])
                g.append([p2.x,p2.y])
        return g
            
    def distancia(self,p2):
        import math
        d = math.sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
        return d