class Ciudad:
  def __init__(self,x,y):
    self.Ciudad=Ciudad
    self.x=x
    self.y=y
  def distancia(self,other):
    d=(((self.x-other.x)**2)+((self.y-other.y)**2))**0.5
    return d 
    
  def camino(self,other):
    pasos=[]
    x=self.x
    y=self.y
    w=other.x
    z=other.y
    if self.x>other.x and self.y>other.y:
     n=0
     while x!=w-1 and y!=z-1:
      pasos.append([x-n,y-n])
      x=x-n
      y=y-n
      n-=1
    elif self.x<other.x and self.y<other.y:
     n=0
     while x!=w+1 and y!=z+1:
      pasos.append([x+n,y+n])
      x=x+n
      y=y+n
      n+=1
    pasos.remove(pasos[-2])  
    pasos.append([w,z])  
    return pasos  
      

if __name__ == "__main__":
  pass
         