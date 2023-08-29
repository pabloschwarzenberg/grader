import math
class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def camino(self,otro):
        ca=[]
        dx=otro.x-self.x
        dy=otro.y-self.y
        xi=self.x
        xf=otro.x
        yi=self.y
        yf=otro.y
        l=[]
        if dx==dy:
            xi=xi-1
            yi=yi-1
            while xf!=xi and yf!=yi:
                xi=xi+1
                l.append(xi)
                yi=yi+1
                l.append(yi)
                ca.append(l)
                l=[]

        else:
            xi=xi-1
            yi=yi-1
            while xi!=xf:
                xi=xi+1
                l.append(xi)
                yi=yi
                l.append(yi)
                ca.append(l)
                l=[]
            while yi!=yf:
                xi=xi
                l.append(xi)
                yi=yi+1
                l.append(yi)
                ca.append(l)
                l=[]
        return ca


    def distancia(self,otro):
        dx=otro.x-self.x
        dy=otro.y-self.y
        d2=dx*dx+dy*dy
        d=math.sqrt(d2)
        return(d)
        
         