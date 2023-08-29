class Ciudad:
    def __init__(self,x,y):
        self.x=int(x)
        self.y=int(y)

    def camino(self,other):
        pasos=[[self.x,self.y]]

        while self.x>other.x:
            pasos.append([(other.x)+1,pasos[-1][1]])
        while self.x<other.x:
            pasos.append([(self.x)+1,pasos[-1][1]])
        while self.y>other.y:
            pasos.append([pasos[-1][0],(other.y)+1])
        while self.y<other.y:
            pasos.append([pasos[-1][0],(self.y)+1])
        return pasos

    def distancia(self,other):
        distancia = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distancia
        
if __name__ == "__main__":
  pass
         