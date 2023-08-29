from math import sqrt

class Ciudad:
    def __init__(self,x,y):
        self.r=[x,y]
            
    def camino(self,other):
        camino=[self.r]
        R=self.r.copy()
        while R!=other.r:
            if R[0]<other.r[0]:
                R[0]+=1
            elif R[0]>other.r[0]:
                R[0]-=1
            if R[1]<other.r[1]:
                R[1]+=1
            elif R[1]>other.r[1]:
                R[1]-=1
            camino.append([R[0],R[1]])
        return camino
        
    def distancia(self,other):
        D=(self.r[0]-other.r[0])**2+(self.r[1]-other.r[1])**2
        return sqrt(D)