import math

class Ciudad:

    def __init__(self,p1,p2):
        self.x=p1
        self.y=p2
        self.lista=[]
        self.lista.append([p1,p2])

    def camino(self,otraCiudad):
        self.lista.append([otraCiudad.x,otraCiudad.y])

        punto1=self.lista[0] #este es temuco
        punto2 =self.lista[1] #este es osorno
        resta_x=0

        resta_y=0
        if (punto1[0]>punto2[0]):
            resta_x=punto1[0]-punto2[0]
        else:
            resta_x=punto2[0]-punto1[0]

        if(punto1[1]>punto2[1]):
            resta_y=punto1[1]-punto2[1]
        else:
            resta_y=punto2[1]-punto1[1]

        self.lista=[]
        self.lista.append(punto1)
        self.lista.append([resta_x,resta_y])
        self.lista.append(punto2)
    
    def distancia(self,otraCiudad):
        self.lista.append([otraCiudad.x,otraCiudad.y])
        self.a=(otraCiudad.x-self.x)**2
        self.b=(otraCiudad.y-self.x)**2
        self.c=sqrt(a+b)
        return self.c