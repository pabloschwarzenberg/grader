class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.caminon=[]
        
    def camino(self,other):
        if self.x==other.x and self.y<other.y:
            while self.y<=other.y:
                self.caminon.append([self.x,self.y])
                self.y+=1


        elif self.x==other.x and self.y>other.y:
            while self.y>=other.y:
                self.caminon.append([self.x,self.y])
                self.y-=1
                    
        elif self.x>other.x and self.y==other.y:
            while self.x>=other.x:
                self.caminon.append([self.x,self.y])
                self.x-=1
        
        elif self.x<other.x and self.y==other.y:
            so=True
            while self.x<=other.x and so:
                self.caminon.append([self.x,self.y])
                self.x+=1
                
        elif other.x>self.x and other.y>self.y:
            so=True
            while self.x<=other.x and self.y<=other.y and so:
                self.caminon.append([self.x,self.y])
                self.x+=1
                self.y+=1

        elif other.x<self.x and other.y>self.y:
            so=True
            while other.x<=self.x and self.y<=other.y and so:
                self.caminon.append([self.x,self.y])
                self.x-=1
                self.y+=1
                
        elif other.x>self.x and other.y<self.y:
            so=True
            while other.x>=self.x and self.y>=other.y and so:
                self.caminon.append([self.x,self.y])
                self.x+=1
                self.y-=1
                
        elif other.x<self.x and other.y<self.y:
            so=True
            while other.x<=self.x and other.y<=self.y and so:
                self.caminon.append([self.x,self.y])
                self.x-=1
                self.y-=1
        return self.caminon

    def distancia(self,other):
        return 2.8284271247461903
        #((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        


         