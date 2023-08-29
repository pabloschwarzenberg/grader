class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def distancia(self,other):
      import math
      distancia=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
      return distancia
  def camino(self,other):
     self.camino=[[self.x,self.y]]
     a=self.x
     b=self.y
     c=other.x
     d=other.y
     while b!=d or a!=c:
           if a<c:
              a+=1
           if a>c:
              a-=1
           if b<d:
              b+=1
           if b>d:
              b-=1
           sublistapuntos=[a,b]
     self.camino.append(sublistapuntos)
     return self.camino

if __name__ == "__main__":
  pass
         