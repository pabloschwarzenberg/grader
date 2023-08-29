class Ciudad:
    def __init__(self,x,y,camino):
        self.x = x
        self.y = y
        self.camino = []

    def distancia(self,p2):
        distancia = math.sqrt(self.x**2+self.y**2)
        return distancia


p1 = Ciudad(3,4,[1,1])
p2 = Ciudad(3,5,[1,2])

if __name__ == "__main__":
  
   print(p1.distancia(p2))
  
         