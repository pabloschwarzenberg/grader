import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,other):
        p_h=math.fabs((self.x)-(other.x))
        p_v=math.fabs((self.y)-(other.y))
        camino=[[self.x,self.y],[p_h,p_v],[other.x,other.y]]
        
        return camino

    def distancia(self,other):
        distancia=float(math.sqrt(((self.x-other.x)**2)+((self.y-other.y)**2)))
        return distancia 
        

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.camino(p2))
    print(p1.distancia(p2))
