import math
class Ciudad:
    #esta variable debiera ser local al interior del método
    #si la defines aquí todos los objetos de la clase Ciudad tendrán
    #una misma variable Camino
    #Camino=[]
    def __init__(self,ciudadx,ciudady):
        self.x=ciudadx
        self.y=ciudady
    def camino(self,other):
        Camino=[]
        Camino.append([self.x,self.y])
        #aquí en este método sucede que como modificas el self.x y el self.y, al terminar
        #el valor self.x y self.y quedarán en la ciudad de destino, perdiéndose los valores
        #originales
        #eso hace que la próxima vez que llames a distancia el cálculo sea erróneo
        #por ejemplo
        #c1=Ciudad(1,1)
        #c2=Ciudad(3,3)
        #c1.camino(c2)
        #al salir de la función c1 será igual a c2 y si calculo la distancia me dará cero
        #en este caso la posición de la ciudad no debiera modificarse como resultado de encontrar un camino
        #porque si se hace eso, la ciudad original se "pierde" y se convierte en la de destino
        #lo cual es un comportamiento inesperado
        #se soluciona creando variables locales
        x=self.x
        y=self.y
        while x!=other.x or y!=other.y:
            if x>other.x and y>other.y:
                x=x-1
                y=y-1
                Camino.append([x,y])
            elif x>other.x and y<other.y:
                x=x-1
                y=y+1
                Camino.append([x,y])
            elif x<other.x and y>other.y:
                x=x+1
                y=y-1
                Camino.append([x,y])
            elif x<other.x and y<other.y:
                x=x+1
                y=y+1
                Camino.append([x,y])
            elif x==other.x and y>other.y:
                y=y-1
                Camino.append([x,y])
            elif x==other.x and y<other.y:
                y=y+1
                Camino.append([x,y])
            elif x>other.x and y==other.y:
                x=x-1
                Camino.append([x,y])
            elif x<other.x and y==other.y:
                x=x+1
                Camino.append([x,y])
        return Camino

    def distancia(self,other):
        d=float(math.sqrt((self.x-other.x)**2+(self.y-other.y)**2))
        return d
if __name__ == "__main__":
   p1=Ciudad(1,1)
   p2=Ciudad(3,3)
   p1.distancia(p2)
   p1.camino(p2)        