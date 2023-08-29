class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def camino(self,other):
    pasos = [[self.x,self.y]]
    tempx = self.x
    tempy = self.y

    while tempx != other.x or tempy != other.y:
        if other.x > tempx and other.y > tempy:
            tempx +=1
            tempy +=1
            pasos.append([tempx,tempy])

        elif other.x > tempx and other.y == tempy:
            tempx +=1
            pasos.append([tempx,tempy])
        elif other.x == tempy and other.y > tempy:
            tempy +=1
            pasos.append([tempx,tempy])

        elif other.x < tempx and other.y < tempy:
            tempx -=1
            tempy -=1
            pasos.append([tempx,tempy])

        elif other.x < tempx and other.y == tempy:
            tempx -= 1
            pasos.append([tempx,tempy])
            
        elif other.x < tempx and other.y > tempy:
            tempx -= 1
            tempy += 1
            pasos.append([tempx,tempy])

        elif other.x == tempx and other.y > tempy:
            tempy += 1
            pasos.append([tempx,tempy])

        elif other.x == tempx and other.y < tempy:
            tempy -=1
            pasos.append([tempx,tempy])
    return pasos

  def distancia(self,other):
      dis = ((other.x - self.x)**2 + (other.y - self.y) **2) ** 0.5
      return dis
            
 
if __name__ == "__main__":
  pass
            
            
           
  
         