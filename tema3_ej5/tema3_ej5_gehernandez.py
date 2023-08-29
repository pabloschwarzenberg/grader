import math
class Ciudad:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
    
    def camino(other,x1,y1):
        i=0
        lista=[]
        [self.x1]=self.x1
        [self.y1]=self.y1
        while i<=len([self.x1]):
            if [self.x1]<=[other.x2]:
                [self.x1]=[self.x1+i]
                listax=[self.x1]
                if [self.y1]<=[other.y2]:
                    [self.x1]=[self.y1+i]
                    listay=[self.y1]
            listax=[ejex]
            listay=[ejey]
            lista=append.lista([listax],[listay])
            i+=i
        return lista
    
    def distancia(x1,y1):
        dist=math.sqrt((self.x1-other.x2)**2 + (self.y1-other.y2)**2)
        return dist
        
if __name__== "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    p1.camino(p2)
    p1.distancia(p2)