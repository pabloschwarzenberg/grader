from math import sqrt
class Ciudad:
  def __init__(self,x,y):
      self.x = x
      self.y = y

  def recorrido(self,other):
        camino = []
        aux = 0
        if self.x == self.y and other.x == other.y:
            aux = abs(other.y-self.y)
            i = 0
            while i<=aux:
                camino.append([])
                i = i + 1
            if self.x<other.x:
                    for i in range(len(camino)):
                        camino[i].append(self.x)
                        camino[i].append(self.y)
                        self.x = self.x + 1
                        self.y = self.y + 1
                    self.x = self.x - aux - 1
                    self.y = self.y - aux - 1
                    return camino
            if self.x>other.x:
                    for i in range(len(camino)):
                        camino[i].append(self.x)
                        camino[i].append(self.y)
                        self.x = self.x - 1
                        self.y = self.y - 1
                    self.x = self.x + aux + 1
                    self.y = self.y + aux + 1
                    return camino

        if self.x == other.x and self.y != other.y:
            aux2 = abs(other.y-self.y)
            j = 0
            while j<=aux2:
                camino.append([])
                j = j + 1
            if self.y<other.y:
                    for j in range(len(camino)):
                      camino[j].append(self.x)
                      camino[j].append(self.y)
                      self.x = self.x
                      self.y = self.y + 1
                    self.y = self.y - aux2 - 1
                    return camino
            if self.y>other.y:
                    for j in range(len(camino)):
                      camino[j].append(self.x)
                      camino[j].append(self.y)
                      self.x = self.x
                      self.y = self.y - 1
                    self.y = self.y + aux2 + 1
                    return camino

        if self.y == other.y and self.x != other.x:
            aux3 = abs(other.x-self.x)
            k = 0
            while k<=aux3:
                camino.append([])
                k = k + 1
            if self.x<other.x:
                    for j in range(len(camino)):
                      camino[j].append(self.x)
                      camino[j].append(self.y)
                      self.x = self.x + 1
                      self.y = self.y
                    self.x = self.x - aux3 - 1
                    return camino

            if self.x>other.x:
                    for j in range(len(camino)):
                      camino[j].append(self.x)
                      camino[j].append(self.y)
                      self.x = self.x - 1
                      self.y = self.y
                    self.x = self.x + aux3 + 1
                    return camino

        if self.x != other.x and self.y != other.y:
            dif_x = abs(other.x-self.x)
            dif_y = abs(other.y-self.y)
            m = 0
            n = 0
            while m<=dif_x:
                camino.append([])
                m = m + 1
            while n<=dif_y:
                camino.append([])
                n = n + 1
            
            
            
        
            
                
            
        
    
  def distancia(self,other):
      X1 = self.x
      X2 = other.x
      Y1 = self.y
      Y2 = other.y
      d = sqrt((X2-X1)**(2) + (Y2-Y1)**(2))
      return d
if __name__ == "__main__":
  c1 = Ciudad(-5,-5)
  c2 = Ciudad(10,10)
  print(c1.recorrido(c2))
  print(c1.distancia(c2))
      

         