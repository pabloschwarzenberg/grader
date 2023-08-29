import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__(self,other):
        #r=Ciudad(0,0)
        a=self.x-other.x  #r.x=
        b=self.y-other.y  #r.y=
        dist=a**2+b**2
        return dist
    
    
    def camino(self,punto):
        lista_puntos=[]
        lista_final=[]
        punto_inicio=[]
        punto_final=[]
        punto_inicio.append(self.x)
        punto_inicio.append(self.y)
        punto_final.append(punto.x)
        punto_final.append(punto.y)
        for i in range(punto.x):
            #print("i:"+str(i))
            if self.x+i==punto.x:
                lista_puntos.append(i)
            
        for j in range(punto.y):
            #print("j:"+str(j))
            if self.y+j==punto.x:
                lista_puntos.append(j)
        
        #print(lista_puntos)
        lista_final.append(punto_inicio)
        lista_final.append(lista_puntos)
        lista_final.append(punto_final)
        return lista_final

    def distancia(self,punto):
        dist=p1-p2
        distancia_final=math.sqrt(dist)
        #distancia_final=round(distancia_final,2)
        return distancia_final
        #return "{0:.2f}".format(distancia_final)    

p1=Ciudad(1,1)
p2=Ciudad(3,3)
print(p1.distancia(p2))
print(p1.camino(p2))






         