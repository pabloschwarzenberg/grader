import math
class Ciudad:
    def __init__(self,origenx,origeny):
        self.origenx=origenx
        self.origeny=origeny

    def distancia(self,destinox,destinoy):
        dis=math.sqrt((self.origenx-destinox)^2+(self.origeny-destinoy)^2)
        return dis

    def camino(self,destinox,destinoy):
        if (self.origenx - destinox) == 0:
            camino=[]
            if (self.origeny - destinoy)<0:
                dif=abs(self.origeny - destinoy)
                for i in range(self.origeny,self.origeny+dif):
                    j=[self.origenx,i]
                    camino.append(j)
            elif (self.origeny - destinoy)>0:
                dif=abs(self.origeny - destinoy)
                for i in range(self.destinoy,self.destinoy+dif):
                    j=[self.origenx,i]
                    camino.append(j)
                return camino
        elif (self.origeny - destinoy) == 0:
            camino=[]
            if (self.origenx - destinox)<0:
                dif=abs(self.origenx - destinox)
                for i in range(self.origenx,self.origenx+dif):
                    j=[i,self.origeny]
                    camino.append(j)
                return camino
            elif (self.origenx - destinox)>0:
                dif=abs(self.origenx - destinox)
                for i in range(self.destinox,self.destinox+dif):
                    j=[i,self.origeny]
                    camino.append(j)
                return camino
        elif (self.origeny - destinoy) == 0 and (self.origenx - destinox) == 0:
            camino=[selforigenx,selforigeny]
            return camino
if __name__ == "__main__":
  pass
         