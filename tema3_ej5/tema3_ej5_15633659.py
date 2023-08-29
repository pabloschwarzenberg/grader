class Ciudad:
  def __init__(self,xa,ya):
    self.xa=xa
    self.ya=ya
  def distancia(self,ciudad):
    dc=(ciudad.xa-self.xa)**2+(ciudad.ya-self.ya)**2
    d=dc**(1/2)
    return d
  def camino(self,ciudad):
    lista=[]
    x=self.xa
    y=self.ya
    lista.append([x,y])
    while x<ciudad.xa:
      x=x+1
      pte=((ciudad.ya-self.ya)/(ciudad.xa-self.xa))
      y=y+pte
      lista.append([x,y])
    return lista
  pass

if __name__ == "__main__":
  xa=float(input("ingrese coordenada x para la ciudad 1:"))
  ya=float(input("ingrese coordenada y para la ciudad 1:"))
  xb=float(input("ingrese coordenada x para la ciudad 2:"))
  yb=float(input("ingrese coordenada y para la ciudad 2:"))
  P1=Ciudad(xa,ya)
  P2=Ciudad(xb,yb)
  print(P1.distancia(P2))
  print(Ciudad.lista(P1,P2))
  pass
         