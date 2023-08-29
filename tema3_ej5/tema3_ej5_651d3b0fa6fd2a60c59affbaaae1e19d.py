class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    #esto es necesario porque para buscar el camino
    #no se debiera mover la posición de la ciudad
    x=self.x
    y=self.y
    d=[[x,y]]
    if x>other.x:
      if y>other.y:
        while True:
          x=x-1
          y=y-1
          d.append([x,y])
          if x==other.x:
            break
          if y==other.y:
            break
      else:
        while True:
          x=x-1
          y=y+1
          d.append([x,y])
          if x==other.x:
            break
          if y==other.y:
            break
    else:
      if y>other.y:
        while True:
          x=x+1
          y=y-1
          d.append([x,y])
          if x==other.x:
            break
          if y==other.y:
            break
      else:
        while True:
          x=x+1
          y=y+1
          d.append([x,y])
          if x==other.x:
            break
          if y==other.y:
            break
    if x==other.x:
      if y>other.y:
        while True:
          y=y-1
          d.append([x,y])
          if y==other.y:
            break
      if y<other.y:
        while True:
          y=y-1
          d.append([x,y])
          if y==other.y:
            break
    if y==other.y:
      if x>other.x:
        while True:
          x=self.x-1
          d.append([x,y])
          if x==other.x:
            break
      if x<other.x:
        while True:
          x=x-1
          d.append([x,y])
          if x==other.x:
            break
    return d
  def distancia(self,other):
    dis=(((self.x-other.x)**2) +((self.y-other.y)**2))**(1/2)
    #dis=round(dis,2)
    return dis
if __name__ == "__main__":
  pass
         