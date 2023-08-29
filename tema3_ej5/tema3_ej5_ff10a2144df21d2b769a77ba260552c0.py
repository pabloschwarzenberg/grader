import math

def obtener_camino(inicio,final):
    camino=[]
    inicio_x=inicio[0]
    inicio_y=inicio[1]
    final_x=final[0]
    final_y=final[1]
    distancia_x=final_x-inicio_x
    distancia_y=final_y-inicio_y
    i=0
    while i<=2:
        l=[]
        l.append(final_x)
        l.append(final_y)
        camino.append(l)
        final_x=final_x-1
        final_y=final_y-1
        i=i+1
        
    return camino



class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def camino(self,other):
        objetivo=[other.x,other.y]
        inicio=[self.x,self.y]
        dist_x=other.x-self.x
        dist_y=other.y-self.x

        camino=obtener_camino(inicio,objetivo)
        camino.sort()
        return camino

    def distancia(self,other):
        distancia=math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        return distancia
        

p1=Ciudad(1,1)
p2=Ciudad(3,3)
print(p1.camino(p2))
print(p1.distancia(p2))


         