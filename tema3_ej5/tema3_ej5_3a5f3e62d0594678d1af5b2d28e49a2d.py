class Ciudad:
  def __init__(self,x,y):
    self.punts=[]
    self.x=x
    self.y=y
  def camino(self,otro):
    posx = self.x
    posy = self.y
    
    while True: 
      if posx<=otro.x and posy<otro.y:
        self.punts.append([posx,posy])
        posx=posx+1
        posy=posy+1
      elif posx>=otro.x and posy<otro.y:
        self.punts.append([posx,posy])
        posy=posy+1
        self.punts.append([self.x,self,y])
      elif posy>=otro.y and posx<otro.x:
        self.punts.append([posx,posy])
        posx=posx+1
      else:
        self.punts.append([posx,posy])
        break
    return self.punts
  def distancia(self,otro):
    return ((self.x-otro.x)**2+(self.y-otro.y)**2)**(1/2)
    
if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)