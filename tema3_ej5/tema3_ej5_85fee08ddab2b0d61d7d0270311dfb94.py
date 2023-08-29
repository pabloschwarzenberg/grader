class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def distancia(self,other):
    r=Ciudad(0,0)
    r.x=(self.x-other.x)**2
    r.y=(self.y-other.y)**2
    d= (r.x+r.y)**(1/2)
    return d
  
    

if __name__ == "__main__":
  pass
         