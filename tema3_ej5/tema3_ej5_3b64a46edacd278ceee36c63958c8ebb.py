class Ciudad:
  def __init__(self,x,y):
    self.posicion = [x,y]
  
  def camino(self,other):
    pos = [self.posicion[0],self.posicion[1]]
    lista = [pos]
    x = pos[0]
    y = pos[1]
    print(pos,other.posicion)
    while(x < other.posicion[0] and y < other.posicion[1]):
      x += 1
      y += 1
      lista.append([x,y])
    while(x < other.posicion[0]):
      x += 1
      lista.append([x,y])
    while(y < other.posicion[1]):
      y += 1
      lista.append([x,y])
    while(x > other.posicion[0] and y > other.posicion[1]):
      x -= 1
      y -= 1
      lista.append([x,y])
    while(x > other.posicion[0]):
      x -= 1
      lista.append([x,y])
    while(y > other.posicion[1]):
      y -= 1
      lista.append([x,y])
    return(lista)

  def distancia(self,other):
    return(((self.posicion[0]-other.posicion[0])**2+(self.posicion[1]-other.posicion[1])**2)**(1/2))

if __name__ == "__main__":
  pass
         