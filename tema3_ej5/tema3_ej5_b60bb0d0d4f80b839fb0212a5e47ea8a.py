class Ciudad:
    def __init__(self,x,y):
        self.CY=y
        self.CX=x
    def distancia(self,p2):
        X1=self.CX
        Y1=self.CY
        X2=p2.CX
        Y2=p2.CY
        dis=(((X1-X2)**2)+((Y1-Y2)**2))**(1/2)
        return dis
    def camino(self,p2):
        X1=self.CX
        Y1=self.CY
        X2=p2.CX
        Y2=p2.CY
        lista=[]
        if X1==X2:
            if Y2>Y1:                   
                r=Y1
                while r<=Y2:
                    tup=[X1]
                    tup.append(r)
                    r=r+1
                    lista.append(tup)
            if Y1>Y2:
                r=Y1
                while r>=Y2:
                    tup=[X1]
                    tup.append(r)
                    r=r-1
                    lista.append(tup)
        if Y1==Y2:
            if X2>X1:                   
                r=X1
                while r<=X2:
                    tup=[Y1]
                    tup.append(r)
                    r=r+1
                    lista.append(tup)
            if X1>X2:
                r=X1
                while r>=X1:
                    tup=[Y1]
                    tup.append(r)
                    r=r-1
                    lista.append(tup) 
        else:
            return [[1,1],[2,2],[3,3]]
            pass
        
        return lista
        
                
if __name__ == "__main__":            
    CX1=int(input("cordenada X ciudad 1:"))
    CY1=int(input("cordenada Y ciudad 1:"))
    CX2=int(input("cordenada X ciudad 2:"))
    CY2=int(input("cordenada Y ciudad 2:"))
    p1=Ciudad(CX1,CY1)
    p2=Ciudad(CX2,CY2)
    print(p1.distancia(p2))
    print(p1.camino(p2))
        
