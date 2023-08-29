class Ciudad:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def lata(self,p2):
        if p2.a>self.a:
            if p2.b>self.b:
                x=p2.a-self.a
                y=p2.b-self.b
                c1=list(str(self.a))+list(str(self.b))
                c2=list(str(x))+list(str(y))
                c3=list(str(p2.a))+list(str(p2.b))
                camino=[]
                camino.append(c1)
                camino.append(c2)
                camino.append(c3)
                return camino
                
            elif p2.b<self.b:
                x=p2.a-self.a
                y=self.b-p2.b
                c1=list(str(self.a))+list(str(self.b))
                c2=list(str(x))+list(str(y))
                c3=list(str(p2.a))+list(str(p2.b))
                camino=[]
                camino.append(c1)
                camino.append(c2)
                camino.append(c3)
                return camino
                
        elif p2.a<self.a:
            if p2.b>self.b:
                x=self.a-p2.a
                y=p2.b-self.b
                c1=list(str(self.a))+list(str(self.b))
                c2=list(str(x))+list(str(y))
                c3=list(str(p2.a))+list(str(p2.b))
                camino=[]
                camino.append(c1)
                camino.append(c2)
                camino.append(c3)
                return camino
                
            elif p2.b<self.b:
                x=self.a-p2.a
                y=self.b-p2.b
                c1=list(str(self.a))+list(str(self.b))
                c2=list(str(x))+list(str(y))
                c3=list(str(p2.a))+list(str(p2.b))
                choro=[]
                choro.append(c1)
                choro.append(c2)
                choro.append(c3)
                print(choro)
                return choro


    def camino(self,p2):
        c=self.lata(p2)
        nuevoc=[]
        for i in c:
            t=[int(i[0]),int(i[1])]
            nuevoc.append(t)
        return nuevoc

     
            
    def distancia(self,c2):
        distancia=((self.a-c2.a)**2+(self.b-c2.b)**2)**(1/2)
        return distancia
        
if __name__ == "__main__":
  pass