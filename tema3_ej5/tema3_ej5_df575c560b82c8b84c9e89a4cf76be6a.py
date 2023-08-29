import math
class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a = []
        self.b = []
        self.r = x
        self.t = y
    def distancia(self,other):
        a1 = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return a1

    def camino(self,other):
        if self.r > 0 and self.t < 4 and self.y < 4 and self.x > 0:
            while True:
                if self.r == other.x and self.t < other.y:
                    self.a.append(self.r)
                    self.a.append(self.t)
                    self.b.append(self.a)
                    self.a = []
                    self.t = self.t + 1
                elif self.r < other.x and self.t < other.y:
                    self.a.append(self.r)
                    self.a.append(self.t)
                    self.b.append(self.a)
                    self.a = []
                    self.t = self.t + 1
                    self.r = self.r + 1
                elif self.t == other.y and self.r < other.x:
                    self.a.append(self.r)
                    self.a.append(self.t)
                    self.b.append(self.a)
                    self.a = []
                    self.r = self.r + 1
                elif self.t == other.y and self.r == other.x:
                    self.a.append(self.r)
                    self.a.append(self.t)
                    self.b.append(self.a)
                    self.a = []
                    break
        else:
            return False
        print(self.b)



if __name__ == "__main__":
  pass
         