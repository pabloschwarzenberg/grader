class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
    
  def camino(self,ciudad2):
    x=int
    y=int
    u=int
    v=int
    self.ciudad2=Ciudad(u,v)
    camino=[]
    w=int
    z=int
    mitad=Ciudad(w,z)
    inicio=Ciudad(x,y)
    camino.append([x,y])
    camino.append([w,z])
    camino.append([u,v])
    self.camino=camino
  def distancia(self,ciudad2):
    u=int
    v=int
    x=int
    y=int
    self.ciudad2=Ciudad(u,v)
    self.ciudad1=Ciudad(x,y)
    
    distancia=sqrt((x-u)*(x-u)+(y-v)*(y-v))
    self.distnacia=distancia
    
    

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  
  
         