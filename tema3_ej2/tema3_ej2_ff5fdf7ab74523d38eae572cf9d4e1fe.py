import math

class Vectores:
    def __init__(self,x,y,z):
        self.vector=[]
        self.vector.append(int(x))
        self.vector.append(int(y))
        self.vector.append(int(z))

    def norma(self):
        poop=[]
        for elem in self.vector:
            poop.append(elem**2)
        poop=sum(poop)
        norm=math.sqrt(poop)
        return int(norm)

    def __repr__(self):
        return "("+str(self.vector[0])+","+str(self.vector[1])+","+str(self.vector[2])+")"

def suma_vectores(v1,v2):
    u=[]
    u.append(int(v1[1])+int(v2[1]))
    u.append(int(v1[3])+int(v2[3]))
    u.append(int(v1[5])+int(v2[5]))
    v3=Vectores(u[0],u[1],u[2])
    return v3
            
           