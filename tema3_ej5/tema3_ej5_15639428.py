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
        x=self.x1
        y=self.y1
        listi.append([x,y])

        while x<ciudad.x1:
            x=x+1
            m=((ciudad.y1-self.y1)/(ciudad.x1-self.x1))
            y=y+m
            listi.append([x,y])

        return listi
    
        
if __name__=='__main__':
    print('ponga las coordenadas de la ciudad1')
    x1=int(input('ingresa x1: '))
    y1=int(input('ingresa y1:'))
    print('ponga las coordenadas de la ciudad2')
    x2=int(input('ingresa x2:'))
    y2=int(input('ingresa y2:'))
    p1=Ciudad(x1,y1)
    p2=Ciudad(x2,y2)
    print('la distancia entre las ciudades es: ',p1.distancia(p2))
    print('el camino que debes recorrer es:',Ciudad.camino(p1,p2))         