class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        r=Ciudad(0,0)
        r.x=self.x+other.x
        r.y=self.y+other.y
        return r
    
    def __sub__(self,other):
        s=Ciudad(0,0)
        s.x=self.x-other.x
        s.y=self.y-other.y
        return s
        
    def camino(self,other):
        c=[]
        a=[self.x,self.y]
        x2=abs(self.x-other.x)
        y2=abs(self.y-other.y)
        b=[x2,y2]
        d=[other.x,other.y]
        c.append(a)
        c.append(b)
        c.append(d)
        return c
      

    def distancia(self,other):
        d=float(((self.x-other.x)**2+(self.y-other.y)**2)**(1/2))
        return d
        

if __name__ == "__main__":       
    c1=Ciudad(1,1)
    c2=Ciudad(3,3)
    print(c1.camino(c2))
    print(c1.distancia(c2))

 