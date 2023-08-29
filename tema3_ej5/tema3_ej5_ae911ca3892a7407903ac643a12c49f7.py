class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def camino(self,c2):
        xlista=self.x
        ylista=self.y
        listafinal=[]
        a=list(str(xlista)+str(ylista))
        b=""
        c=""
        d=""
        while(xlista!=c2.x and ylista!=c2.y):
            if(self.x<c2.x):
                xlista=xlista+1
            elif(self.y<c2.y):
                ylista=ylista+1
            elif(self.x>c2.x):
                xlista=xlista-1
            elif(self.y<c2.y):
                ylista=ylista-1
            if (b==""):
                b=list(str(xlista)+str(xlista))
            elif (c==""):
                c=list(str(xlista)+str(xlista))
            elif (d==""):
                d=list(str(xlista)+str(xlista))
        listafinal.append(a)
        listafinal.append(b)
        listafinal.append(c)
        
        return listafinal

    def distancia(self,c2):
        if(self.x<c2.x):
            baset=c2.x-self.x
        if(self.y<c2.y):
            alturat=c2.y-self.y
        elif(self.x>c2.x):
            baset=self.x-c2.x
        elif(self.y<c2.y):
            alturat=self.y-c2
        hipotenusat=((baset**2)+(alturat**2))**(1/2)
        return hipotenusat
        

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    b=p1.camino(p2)
    c=p1.distancia(p2)
    print(b)
    print(c)