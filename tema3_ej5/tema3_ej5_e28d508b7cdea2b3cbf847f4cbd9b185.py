class Ciudad:
    def __intit__(self,x,y):
        self.x=int(x)
        self.y=int(y)
    def distancia(self,other):
        x1=self.x
        x2=other.x
        y1=self.y
        y2=other.y
        delta_x=(x1-x2)**2
        delta_y=(y1-y2)**2
        dist=(delta_x+delta_y)**(1/2)
        return dist
    def camino(self,other):
        xi=self.x
        yi=self.y
        xf=other.x
        yf=other.y
        x=[]
        y=[]
        for k in range(xi,xf+1):
            x.append(k)
        for h in range(yi,yf+1):
            y.append(h)
        camino=[]
        for i in range(len(x)):
            paso=[x[i],y[i]]
            camino.append(paso)
        return camino

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  print(p1.camino(p2))
  print(p1.distancia(p2))
  
         