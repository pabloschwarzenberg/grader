import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def camino(self,p2):
    lista=[]
    a=0
    while a<=p2.x and a<=p2.y:
      paso=[]
      self.x=self.x+1
      paso.append(self.x)
      self.y=self.y+1
      paso.append(self.y)
      lista.append(paso)
      a+=1
      
    return lista
    
  def distancia(self,p2):
    x=self.x-p2.x
    y=self.y-p2.y
    distancia=math.sqrt((x**2)+(y**2))
    return distancia
      
      
  pass

if __name__ == "__main__":
  pass
         