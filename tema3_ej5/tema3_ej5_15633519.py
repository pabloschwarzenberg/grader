import math
import copy
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia(self,other):
        r=math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2))
        return r

    def camino(self,other):
        self_copia=copy.copy(self)
        posicion=[]
        posicion.append([self.x,self.y])

        while True:
            if self_copia.x<other.x:
                self_copia.x+=1

            elif self_copia.x>other.x:
                self_copia-=1

            if self_copia.y<other.y:
                self_copia.y+=1

            elif self_copia.y>other.y:
                self_copia.y-=1

            posicion.append([self_copia.x,self_copia.y])
            if self_copia.x==other.x and self_copia.y==other.y:
                break

        return posicion


    def __str__(self):
        return "[{0},{1}]".format(self.x,self.y)


if __name__ == "__main__":
    c=input("Ingrese coordenadas primera ciudad de la forma a,b : ")
    c=c.split(",")
    c1=Ciudad(int(c[0]),int(c[1]))

    c=input("Ingrese coordenadas segunda ciudad de la forma a,b : ")
    c=c.split(",")
    c2=Ciudad(int(c[0]),int(c[1]))

    print(c1.camino(c2))
    print(c1.distancia(c2))