class Ciudad:
  def __init__(self,x,y):
      self.x=x
      self.y=y
  def distancia(self,other):
      a=int(((self.x-other.x)**2+(self.y-other.y)**2)**(1/2))
      print(a)
  def camino(self,other):
      camino=[]
      if self.y > other.y:
        if self.x > other.x:
          camino.append(str(other.x)+","+str(other.y))
          while other.y < self.y:
            while other.x < self.x:
              other.x+=1
              camino.append(str(other.x)+","+str(other.y))
            other.y+=1
            camino.append(str(other.x)+","+str(other.y))
        else:
          camino.append(str(other.x)+","+str(other.y))
          while other.y < self.y:
            while other.x > self.x:
              other.x-=1
              camino.append(str(other.x)+","+str(other.y))
            other.y+=1
            camino.append(str(other.x)+","+str(other.y))
        
      else:
        if self.x > other.x:
          camino.append(str(other.x)+","+str(other.y))
          while other.y > self.y:
            while other.x < self.x:
              other.x+=1
              camino.append(str(other.x)+","+str(other.y))
            other.y-=1
            camino.append(str(other.x)+","+str(other.y))
        else:
          camino.append(str(other.x)+","+str(other.y))
          while other.y > self.y:
            while other.x > self.x:
              other.x-=1
              camino.append(str(other.x)+","+str(other.y))
            other.y-=1
            camino.append(str(other.x)+","+str(other.y))
      print(camino)
      
        
              
              