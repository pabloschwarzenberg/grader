class Ciudad:
  def __init__(self, x, y):
    self.x=x
    self.y=y

    
  def camino(self, coordenada):
    x=coordenada.x
    y=coordenada.y
    distx=int(((self.x-x)**2)**0.5)
    disty=int(((self.y-y)**2)**0.5)
    lista=[]
    i=0
    j=0
    while i<=distx:
        while j<=disty:
          meter=[self.x+i,self.y+j]
          lista.append(meter)
          i+=1
          j+=1
          if j==disty and i==distx:
            break
          if i==distx:
            i-=1
          if j==disty:
            j-=1
    print(lista)
    return lista
        
  def distancia(self, coordenada):
    x=coordenada.x
    y=coordenada.y
    distancia=((self.x-x)**2+(self.y-y)**2)**0.5
    print(distancia)
    return distancia

if __name__ == "__main__":
  pass
         