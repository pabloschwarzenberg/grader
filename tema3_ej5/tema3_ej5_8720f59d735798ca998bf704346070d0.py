import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(p1,p2):
    dx=p2.x-p1.x
    dy=p2.y-p1.y
    if dx==dy:
        r=dx
    elif dx>dy:
        r=dx
    elif dx<dy:
        r=dy
    dx=dx/r
    dy=dy/r
    camino=[]
    paso=[[(p1.x),(p1.y)]]
    camino.extend(paso)
    p1x=p1.x
    p1y=p1.y
    p2x=p2.x
    p2y=p2.y
    while (p1x)!=(p2x) and (p1y)!=(p2y):
        p1x=int(p1x+dx)
        p1y=int(p1y+dy)
        paso=[[(p1x),(p1y)]]
        camino.extend(paso)
    return(camino)
    
  def distancia(p1,p2):
    x=p2.x-p1.x
    y=p2.y-p1.y
    distancia=(math.sqrt((x**2)+(y**2)))
    return(distancia)
      
if __name__ == "__main__":
  p1=Ciudad(input())
  p2=Ciudad(input())
  p1.camino(p2)
  p1.distancia(p2)
  
  
         