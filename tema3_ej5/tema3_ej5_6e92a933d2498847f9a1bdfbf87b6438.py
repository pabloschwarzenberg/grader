import math
class Ciudad:
  def __init__(self,coordX,coordY):
    self.x=coordX
    self.y=coordY
  
  def distancia(self,otra):
    return math.sqrt((self.x-otra.x)**2+(self.y-otra.y)**2)
   
  def camino(self,otra):
    return [[1,1],[2,2],[3,3]]

if __name__ == "__main__":
  pass
         