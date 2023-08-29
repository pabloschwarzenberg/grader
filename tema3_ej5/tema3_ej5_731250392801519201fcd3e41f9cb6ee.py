class Ciudad:
    
    def __init__(self,x,y):
      
        self.x=x
        self.y=y
    def camino(self,other):
        l=[[self.x,self.y]]
        if other.x-self.x>0:
            
            for i in range(1,other.x-self.x+1):
                
                l.append([self.x+i,self.y])
        else:
            for i in range(1,self.x-other.x+1):
                l.append([self.x-i,self.y])
        if other.y-self.y>0:
            for i in range(1,other.y-self.y+1):
                l.append([l[-1][0],self.y+i])
        else:
            for i in range(1,self.y-other.y+1):
                l.append([l[-1][0],self.y-i])
                
        return l
    def distancia(self,other):
        d=(((self.x-other.x)**2)+((self.y-other.y)**2))**(0.5)
        return d
           
     

if __name__ == "__main__":
  pass
         