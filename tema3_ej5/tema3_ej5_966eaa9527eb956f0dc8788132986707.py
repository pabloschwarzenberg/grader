class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def camino(self,other):
        camino = [abs(self.x - other.x),abs(self.y - other.y)]
        points = [[self.x,self.y],camino,[other.x,other.y]]
        return points
    def distancia(self,other):
       distancia= ((self.x-other.x)**2 + (self.y - other.y)**2)**(1/2)
       return distancia

if __name__ == "__main__":
  pass
         