import math

class Ciudad:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
        
    def distancia(self,ciudad):
        
        dist=((ciudad.x1-self.x1)**2+(ciudad.y1-self.y1)**2)**(1/2)
        return dist
    def camino(self,ciudad):
        listi=[]
        X=self.x1
        Y=self.y1
        


        while X<ciudad.x1:
            
            m=int((ciudad.y1-Y)/(ciudad.x1-X))
            listi.append([X,Y])
            X=X+1
            listi.append([ciudad.x1,ciudad.y1])

            return listi
        

if __name__=='__main__':
    print("ingrese cordenadas de la ciudad")
    x1=int(input("x1:"))
    y1=int(input("y1:"))

    c1=Ciudad(x1,y1)

        
    print("ingrese cordenadas de la segunda ciudad")
    x2=int(input("x2:"))
    y2=int(input("y2:"))

    c2=Ciudad(x2,y2)
    print("la distancia entre las ciudades es:")
    print(c1.distancia(c2))
    print(Ciudad.camino(c1,c2))
