class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distancia(self,otra_ciudad):
        dx = self.x - otra_ciudad.x
        dy = self.y - otra_ciudad.y
        return (dx*dx + dy*dy)**0.5
    
    def camino(self,otra_ciudad):
        if self.x == otra_ciudad.x and self.y == otra_ciudad.y:
            return [[self.x,self.y]]
        elif self.x == otra_ciudad.x:
            camino = [[self.x, y] for y in range(min(self.y, otra_ciudad.y), max(self.y, otra_ciudad.y)+1)]
        elif self.y == otra_ciudad.y:
            camino = [[x, self.y] for x in range(min(self.x, otra_ciudad.x), max(self.x, otra_ciudad.x)+1)]
        elif abs(self.x-otra_ciudad.x)==abs(self.y-otra_ciudad.y):
            incx = 1 if self.x < otra_ciudad.x else -1
            incy = 1 if self.y < otra_ciudad.y else -1
            camino = [[self.x+i*incx, self.y+i*incy] for i in range(abs(self.x-otra_ciudad.x)+1)]
        else:
            return None

        if camino[0]!=[self.x,self.y] or camino[-1]!=[otra_ciudad.x,otra_ciudad.y]:
            return None
        else:
            return camino
