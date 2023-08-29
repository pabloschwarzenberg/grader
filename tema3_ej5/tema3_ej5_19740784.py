class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    cam_x=other.x - self.x
    cam_y=other.y - self.y
    cam_x2=-(other.x - self.x)
    cam_y2=-(other.y - self.y)
    return cam_x,cam_y,cam_x2,cam_y2
  def distancia(self):
    cam_x=other.x - self.x
    cam_y=other.y - self.y
    dist=cam_x**2 + cam_y**2
    dist=dist**(1/2)
    return dist

if __name__ == "__main__":
  a=float(input())
  ciu1=Ciudad(a,b)
  c=float(input())
  ciu2=Ciudad(c,d)
  
         