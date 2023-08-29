import math as ma 

class Ciudad: 

    def __init__(self,x,y): 

        self.x=x 

        self.y=y 

     

    def camino(self,p2): 

        puntos=[] 

        puntos2=[] 

        puntos2.append(self.x) 

        puntos2.append(self.y) 

        puntos.append(puntos2) 

        horizontal1=p2.x-self.x 

        vertical1=p2.y-self.y 

        puntos2=[] 

        puntos2.append(horizontal1) 

        puntos2.append(vertical1) 

        puntos.append(puntos2) 

        puntos2=[] 

        puntos2.append(p2.x) 

        puntos2.append(p2.y) 

        puntos.append(puntos2) 

        return puntos 

    def distancia(self,p2): 

        horizontal=p2.x-self.x 

        vertical=p2.y-self.y 

        camino=ma.sqrt((horizontal*2)+(vertical*2)) 

        #camino=str(camino) 

        #camino=camino[0:4] 

        return camino 

 

if __name__ == "__main__": 

    ciudad1=Ciudad(1,1) 

    ciudad2=Ciudad(3,3) 

    print(ciudad1.distancia(ciudad2)) 

    print(ciudad1.camino(ciudad2)) 
         