class Ciudad:
  def __init__(self,coord_1,coord_2):
    self.coord_1=coord_1
    self.coord_2=coord_2

  def camino(self,other):
    lista_mayor=[]
    lista_mayor.append([self.coord_1,self.coord_2])
    x=self.coord_1
    y=self.coord_2
    while (x!=other.coord_1) or (y!= other.coord_2):
      if x > other.coord_1:
        x=x-1
      elif x < other.coord_1:
        x=x+1
      if y > other.coord_2:
        y=y-1
      elif y < other.coord_2:
        y=y+1
      lista_mayor.append([x,y])
    return lista_mayor
  

  def distancia(self,other):
    distancia = ((self.coord_1-other.coord_1)**2 + (self.coord_2-other.coord_2)**2)**(0.5)
    return distancia


if __name__ == "__main__":
  pass
         