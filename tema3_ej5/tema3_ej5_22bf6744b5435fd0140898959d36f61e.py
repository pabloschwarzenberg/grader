from math import sqrt

class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distancia(self,other):
        x1=self.x-other.x
        x2=self.y-other.y
        distancia=sqrt(x1*x1+x2*x2)
        return(distancia.round(2))
        
    def camino(self,other):
        x1=self.x-other.x
        y1=self.y-other.y
        i=1
        j=1
        lista_puntos=[]
        punto=[self.x,self.y]
        lista_puntos.append(punto)
        while True:
            if x1<0 and y1<0:
                punto=[self.x+i,self.y+i]
                
                x1=x1+1
                y1=y1+1
            elif x1>0 and y1>0:
                punto=[self.x-i,self.y-i]
                lista_puntos.append(punto)
                x1=x1-1
                y1=y1-1
            elif x1<0 and y1>0:
                punto=[self.x+i,self.y-i]
                lista_puntos.append(punto)
                x1=x1+1
                y1=y1-1
            elif x1>0 and y1<0:
                punto=[self.x-i,self.y+i]
                lista_puntos.append(punto)
                x1=x1-1
                y1=y1+1
            if x1==0 or y1==0:
                i+=1
                j+=1
                break
            i+=1
            j+=1
        


if __name__ == "__main__":
  pass
         