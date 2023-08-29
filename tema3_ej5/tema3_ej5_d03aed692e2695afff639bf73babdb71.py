class Ciudad:
  def __init__(self,x,y):
  self.x = x
  self.y = y
  self.coordenadas = [x,y]
  def camino(self,other):
    Puntos = []
    if self.y < other.y:
      if self.x < other.x:
        while self.y != other.y and self.x != other.x:
          punto = [self.x+=1,self.y+=1]
          Puntos.append(punto)
        if self.x == other.x:
          while self.y != other.y:
            punto = [self.x,self.y+=1]
            Puntos.append(punto)
        if self.y == other.y:
          while self.x != other.x:
            punto = [self.x += 1,self.y]
            Puntos.append(punto)
      if self.x > other.x:
        while self.y != other.y and self.x != other.x:
          punto = [self.x-=1,self.y+=1]
          Puntos.append(punto)
        if self.x == other.x:
          while self.y != other.y:
            punto = [self.x,self.y+=1]
            Puntos.append(punto)
        if self.y == other.y:
          while self.x != other.x:
            punto = [self.x -= 1,self.y]
            Puntos.append(punto)
    if self.y = other.y:
      while self.x != other.x:
        if self.x < other.x:
          punto = [self.x += 1, self.y]
          Puntos.append(punto)
        if self.x > other.x:
          punto = [self.x -= 1, self.y]
          Puntos.append(punto)
    
    if self.y > other.y:
      if self.x < other.x:
        while self.y != other.y and self.x != other.x:
          punto = [self.x-=1,self.y+=1]
          Puntos.append(punto)
        if self.x == other.x:
          while self.y != other.y:
            punto = [self.x,self.y-=1]
            Puntos.append(punto)
        if self.y == other.y:
          while self.x != other.x:
            punto = [self.x += 1,self.y]
            Puntos.append(punto)
  def distanica(self):
  pass

if __name__ == "__main__":
  pass
         