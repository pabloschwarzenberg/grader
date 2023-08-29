class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return distancia(self,other)
    def distancia(self,other):
        distancia=(((self.x - other.x)**2 + (self.y-other.y)**2 +(self.z-other.z)**2)**1/2)
        return distancia
    def camino(self,other):
        lista=[]
        for i in range(self.x - other.x):
            for j in range(self.y -other.y):
                pos=[i,j]
                lista.append(pos)
        return lista