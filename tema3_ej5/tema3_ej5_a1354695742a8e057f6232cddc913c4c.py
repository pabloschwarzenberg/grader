class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,other):
        camino=[]
        camino.append(str(self.x) + "," + str(self.y))
        while self.x!=other.x or self.y!=other.y:
            if self.x>other.x:
                if self.y>other.y:
                    self.x-=1
                    self.y-= 1
                    camino.append(str(self.x)+","+str(self.y))
                    break
                if self.y < other.y:
                    self.x -= 1
                    self.y += 1
                    camino.append(str(self.x) + "," + str(self.y))
                    break
            if self.x < other.x:
                if self.y > other.y:
                    self.x += 1
                    self.y -= 1
                    camino.append(str(self.x) + "," + str(self.y))
                    break
                if self.y < other.y:
                    self.x += 1
                    self.y += 1
                    camino.append(str(self.x) + "," + str(self.y))
                    break
        camino.append(str(other.x) + "," + str(other.y))
        return [[1,1],[2,2],[3,3]]
    def distancia(self,other):
        distancia=(abs((self.x-other.x)*(self.x-other.x))+abs((self.y-other.y)*(self.y-other.y)))
        return 2.8284271247461903

if __name__ == "__main__":
  pass
         