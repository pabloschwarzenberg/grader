class Ciudad:
  def __init__(self,x,y,camino):
    self.x=x
    self.y=y
    self.camino=camino
  def _posicion_relativa__(self,other):
    if self.x>other.x:
      dx=-1
    elif self.x==other.x:
      dx=0
    else:
      dx=1
    if self.y>other.y:
      dy=-1
    elif self.y==other.y:
      dy=0
    else:
      dy=1
    return dx,dy
  def __camino__(self,other):
    camino=[]
    while self.x!=other.x and self.y!=other.y:
      self.x+=dx
      self.y+=dy
      camino.append([self.x,self.y])
      
  def __distancia__(self,other):
    self.camino=[]
    self.desplazamiento=0
    while self.x!=other.x and self.y!=other.y:
      self.x+dx
      self.y+dy
      camino.append([self.x,self.y])
      desplazamiento+=2**(1/2)
   
  def __str__(self):
     return self.camino, self.desplazamiento

if __name__ == "__main__":
  pass
         