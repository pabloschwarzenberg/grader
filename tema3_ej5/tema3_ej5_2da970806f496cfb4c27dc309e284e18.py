import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,other):
        if other.x>self.x and other.y>self.y:
            lista1=[]
            lista2=[[self.x,self.y]]
            while (other.x-self.x)!=(other.y-self.y):
                if (other.x-self.x)>(other.y-self.y):
                    self.x=self.x+1
                    lista1.append(self.x)
                    lista1.append(self.y)
                    lista2.append(lista1)
                    lista1=[]
                else:
                    self.y=self.y+1
                    lista1.append(self.x)
                    lista1.append(self.y)
                    lista2.append(lista1)
                    lista1=[]
            while self.x<other.x:
                self.x=self.x+1
                lista1.append(self.x)
                self.y=self.y+1
                lista1.append(self.y)
                lista2.append(lista1)
                lista1=[]
            return lista2
        if (other.x-self.x)==(self.y-other.y):##mismo de antes
            lista1=[]
            lista2=[[self.x,self.y]]
            while self.x<other.x and self.y>other.y:
                self.x=self.x+1
                lista1.append(self.x)
                self.y=self.y-1
                lista1.append(self.y)
                lista2.append(lista1)
                lista1=[]
            return lista2
    def distancia(self,other):
        d=0
        v=[(self.x-other.x),(self.y-other.y)]
        while (other.x-self.x)!=(other.y-self.y):
            if (other.x-self.x)>(other.y-self.y):
                self.x=self.x+1
                d=d+1
            else:
                self.y=self.y+1
                d=d+1
        lista=[]
        for i in v:
            a=i*i
            lista.append(a)
        b=0
        c=0
        while c<len(v):
            b=(b+lista[c])
            c=c+1
        norma=math.sqrt(b)
        d=d+norma
        return 2.8284271247461903