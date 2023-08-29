import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,otro):
        pasosx=[]
        pasosy=[]
        if self.x<otro.x:
            for i in range(self.x,otro.x+1):
                if abs(i)-abs(int(i))==0:
                    pasosx.append(i)
        elif self.x>otro.x:
            for i in range(otro.x,self.x+1):
                if abs(i)-abs(int(i))==0:
                    pasosx.append(i)
        if self.y<otro.y:
            for i in range(self.y,otro.y+1):
                if abs(i)-abs(int(i))==0:
                    pasosy.append(i)
        elif self.y>otro.y:
            for i in range(otro.y,self.y+1):
                if abs(i)-abs(int(i))==0:
                    pasosy.append(i)
        for i in range(0,len(pasosx)):
            e=pasosx[i],pasosy[i]
            pasosx[i]=list(e)
        for i in pasosx:
            if len(i)==1:
                pasosx.pop(pasosx.index(i))
        return pasosx
    def distancia(self,otro):
        distancia=math.sqrt((self.x-otro.x)**2+(self.y-otro.y)**2)
        return distancia 
        
        

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.distancia(p2))
    print(p1.camino(p2))
