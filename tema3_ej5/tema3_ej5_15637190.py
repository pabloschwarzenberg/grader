class Ciudad:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def camino(self,Ciudad):
        lista=[]
        for i in range(self.x,Ciudad.x):
           i+=1
           for j in range(self.y,Ciudad.y):
             j+=1
             lista.append([i,j])
        print(lista)
             

if __name__ == "__main__":
  pass
         