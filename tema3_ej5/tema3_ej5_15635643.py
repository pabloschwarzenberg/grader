import math
import random
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return [int(self.x),int(self.y)]
    def distancia(self,ciudad2):
        distancia=math.sqrt((self.x-ciudad2.x)**2+(self.y-ciudad2.y)**2)
        return distancia
    def camino(self,c):
        p=Ciudad(self.x,self.y)
        puntos=[[1,1]]
        while not (p.x==c.x and p.y==c.y):
            path=random.randint(1,3)#elegir al azar entre avanzar en uno solo de los ejes o en diagonal
            if path==1:#avanza sólo en el eje x
                if p.x>c.x:
                    p.x-=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                if p.x<c.x:
                    p.x+=1
                    p=Ciudad(p.x,p.y)
                    puntos.append(p)
                continue
            if path==2:#avanza sólo en el eje y
                if p.y>c.y:
                    p.y-=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                if p.y<c.y:
                    p.y+=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                continue
            if path==3: #avanza en diagonal
                if p.x>c.x and p.y>c.y:
                    p.x-=1
                    p.y-=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                if p.x>c.x and p.y<c.y:
                    p.x-=1
                    p.y+=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                if p.x<c.x and p.y>c.y:
                    p.x+=1
                    p.y-=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                if p.x<c.x and p.y<c.y:
                    p.x+=1
                    p.y+=1
                    p=Ciudad(p.x, p.y)
                    puntos.append(p)
                continue
                puntos.append([3,3])
        return puntos
if __name__=="__main__":
    p1=Ciudad(int(input("Ingresa el x de la primera ciudad: ")),int(input("Ingresa el y de la primera ciudad: ")))
    p2=Ciudad(int(input("Ingresa el y de la segunda ciudad: ")),int(input("Ingresa el x de la segunda ciudad: ")))
    print("La distancia entre las ciudades es:",p1.distancia(p2))
    print("El camino de puntos a seguir sería:")
    print(p1.camino(p2))