import math
class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xy = []
    
    def distancia(self,p2):
        k = (self.x -p2.x)**2 + (self.y -p2.y)**2        
        a = math.sqrt(k)
        return a
    def camino(self,p2):
        if self.distancia(p2) == 0:
            self.xy.append([self.x,self.y])
            return self.xy
        else:
            self.xy.append([self.x,self.y])
            difx = abs(p2.x - self.x)
            dify = abs(p2.y - self.y)
            h = 0
            i = 0
            j = 0
            l = 0
            while h <= difx-1:
                pasox = self.x + j
                j = j + 1
                h = h + 1
            while i <= dify-1:
                pasoy = self.y + l
                l = l + 1
                i = i + 1
            self.xy.append([pasox,pasoy])
            self.xy.append([p2.x,p2.y])
            return self.xy