import math
class Ciudad:
    def __init(self,x,y):
        self.x = x
        self.y = y
        
    def distancia(self,other):
        x = float(self.x - other.x)
        y = float(self.y - other.y)

        d = math.sqrt(x ** 2 + y ** 2)
        return d

if __name__ == "__main__":
  pass
         