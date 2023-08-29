class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def camino(self,other):
    listax = []
    i = self.x
    while i < other.x:
      listax.append(i)
      i += 1
    listay = []
    i = self.y
    while i < other.y:
      listay.append(i)
      i += 1
    if len(listay) < len(listax):
      while len(listay) != len(listax):
        listay.append(0)
    elif len(listay) > len(listax):
      while len(listay) != len(listax):
        listax.append(0)
    lista = []
    for elemento in range(len(listax)):
      lista.append([listax[elemento],listay[elemento]])
    lista.append([other.x,other.y])
    return lista
  def distancia(self,other):
    a = other.x - self.x
    b = other.y - self.y
    d = ((a)**2 + (b)**2)**(1/2)
    return d
    
      
    