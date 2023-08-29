class Ciudad:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
    def camino(self,A):
        L=[[self.X,self.Y]]
        C=min(abs(self.X-A.X),abs(self.Y-A.Y))
        for i in range(C):
            self.X+=1;self.Y+=1
            L.append([self.X,self.Y])
        s=C*2**0.5
        if self.X==A.X:
            for i in range(A.Y-self.Y):
                self.Y+=1
                L.append([self.X,self.Y])
                s=s+A.Y-self.Y
        else:
            for i in range(A.X-self.X):
                self.X+=1
                L.append([self.X,self.Y])
                s=s+A.X-self.X
        self.distancia=s 
        print(L)
        return str(s)        
