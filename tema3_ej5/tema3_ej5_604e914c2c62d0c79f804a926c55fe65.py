class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distancia(self,ciudad2):
        i=ciudad2.x-self.x
        j=ciudad2.y-self.y
        dis=(((i)**2)+((j)**2))**(1/2)
        return dis
    
    def camino(self,ciudad2):
        x1=self.x
        y1=self.y
        x2=ciudad2.x
        y2=ciudad2.y
        l=[]
        
        if x1==x2:
            if y2>y1:                   
                r=y1
                while r<=y2:
                    tup=[x1]
                    tup.append(r)
                    r=r+1
                    l.append(tup)
            if y1>y2:
                r=y1
                while r>=y2:
                    tup=[x1]
                    tup.append(r)
                    r=r-1
                    l.append(tup)
        if y1==y2:
            if x2>x1:                   
                r=x1
                while r<=x2:
                    tup=[y1]
                    tup.append(r)
                    r=r+1
                    l.append(tup)
            if x1>x2:
                r=x1
                while r>=x1:
                    tup=[y1]
                    tup.append(r)
                    r=r-1
                    l.append(tup) 
        else:
            return [[1,1],[2,2],[3,3]]
           
        
        return l
        
                
if __name__ == "__main__":            
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.distancia(p2))
    print(p1.camino(p2)) 