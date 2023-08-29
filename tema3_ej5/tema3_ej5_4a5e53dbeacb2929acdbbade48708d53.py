class Ciudad:
    def __init__(self,x,y):
       self.x=x
       self.y=y
    def camino(self,otra):
        camino=[]
        x=otra.x-self.x
        y=otra.y-self.y
        listax=[]
        listay=[]
        for a in range(1,abs(x)+1):
            listax.append(a*(x//abs(x)))
        for a in range(1,abs(y)+1):
            listay.append(a*(y//abs(y)))
        if(abs(x)>abs(y)):
            for a in range(abs(y)+1,abs(x)+1):
                listay.append(y)
        if(abs(x)<abs(y)):
            for a in range(abs(x)+1,abs(y)+1):
                listax.append(x)
        camino.append([self.x,self.y])
        for a in range(len(listax)):
          camino.append([listax[a]+self.x,listay[a]+self.y])
        return(camino)
                    
    def distancia(self,otra):
        x=self.x-otra.x
        y=self.y-otra.y
        return (((x**2+y**2)**(1/2)))

if __name__ == "__main__":
  pass
         