import math

class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.norma=0
      
    def camino(self,otra_ciudad):
        lista=[]
    
        a=self.x
        b=self.y
        if self.x<otra_ciudad.x and self.y<otra_ciudad.y:
            while True:
                listita=[]
                try:
                    listita.append(a)
                    listita.append(b)
                    lista.append(listita)
                    a+=1
                    b+=1
                    #print(a)
                    #print(listita)
                    #print(lista)
                    if a>otra_ciudad.x or b>otra_ciudad.y:
                        break
                except:
                    break

        elif self.x<otra_ciudad.x and self.y<otra_ciudad.y:
            while True:
                listita=[]
                try:
                    listita.append(a)
                    listita.append(b)
                    lista.append(listita)
                    a-=1
                    b-=1
                    #print(a)
                    #print(listita)
                    #print(lista)
                    if a<otra_ciudad.x or b>otra_ciudad.y:
                        break
                except:
                    break
        elif self.x<otra_ciudad.x and self.y>otra_ciudad.y:
            while True:
                listita=[]
                try:
                    listita.append(a)
                    listita.append(b)
                    lista.append(listita)
                    a+=1
                    b-=1
                    #print(a)
                    #print(listita)
                    #print(lista)
                    if a>otra_ciudad.x or b<otra_ciudad.y:
                        break
                except:
                    break
        else:
            while True:
                listita=[]
                try:
                    listita.append(a)
                    listita.append(b)
                    lista.append(listita)
                    a-=1
                    
                    #print(a)
                    #print(listita)
                    #print(lista)
                    if a<otra_ciudad.x or b>otra_ciudad.y:
                        break
                except:
                    break
        return lista

        
     
    def distancia(self, otra_ciudad):
        a=(self.x-otra_ciudad.x)**2 + (self.y-otra_ciudad.y)**2
        self.norma=math.sqrt(a)
        return self.norma
#a=input()
#b=input()
#c=input()
#d=input()
#p1=Ciudad(a,b)
#p2=Ciudad(c,d)


        