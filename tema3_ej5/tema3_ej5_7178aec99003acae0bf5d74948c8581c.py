class Ciudad():
  def __init__(self, x, y):
    self.x=x
    self.y=y
  def camino(self, other):
    a=[[]]
    x=self.x
    y=self.y
    while x!=other.x or y!=other.y:
      if x<other.x and y<other.y:
        a.append([x+1, y+1])
        x=x+1
        y=y+1
      if x>other.x and y>other.y:
        a.append([x-1, y-1])
        x=x-1
        y=y-1
      if x<other.x and y>other.y:
        a.append([x+1, y-1])
        x=x+1
        y=y-1
      if x>other.x and y<other.y:
        a.append([x-1, y+1])
        x=x-1
        y=y+1
      if x<other.x and y==other.y:
        a.append([x+1, y])
        x=x+1
      if x>other.x and y==other.y:
        a.append([x-1, y])
        x=x-1       
      if x==other.x and y<other.y:
        a.append([x, y+1])
        y=y+1
      if x==other.x and y>other.y:
        a.append([x, y-1])
        y=y-1
    print(a)
  def distancia(self, other):
    print(((self.x-other.x)**2 + (self.y-other.y)**2)**(0.5))
  pass

if __name__ == "__main__":
  pass
         