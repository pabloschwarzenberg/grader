class Ciudad:
  def __init__(self,x,y):
      self.x= x
      self.y=y    
  def distancia(self,other):
      distancia=((self.x-other.x)^2+(self.y-other.y)^2)^1/2
      return distancia
  def lista_puntos(self,other):
      return [[1,1],[2,2],[3,3]]
         