import math

class Ciudad:
  def __init__(self,x,y):
      self.camino_list=[]
      self.x=x
      self.y=y
      
  def camino(self,ciudad):
      a=abs(self.x-ciudad.x)
      b=abs(self.y-ciudad.y)
      c=[a,b]
      d=[self.x,self.y]
      e=[ciudad.x,ciudad.y]
      self.camino_list.append(d)
      self.camino_list.append(c)
      self.camino_list.append(e)
      return self.camino_list

  def distancia(self,ciudad):
      d=math.sqrt((self.x-ciudad.x)**2+(self.y-ciudad.y)**2)
      return d

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)
         