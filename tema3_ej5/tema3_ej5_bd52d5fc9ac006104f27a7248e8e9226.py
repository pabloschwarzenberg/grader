class Ciudad:
  def __init__(self,matriza,matrizb):  
      self.matriza=matriza
      self.matrizb=matrizb
    
  def caminos(self):
    m=int(len(self.matriza))
    n=int(len(self.matriza[0]))
    c=[]
    for i in range(m):
      fila=[]
      for j in range(n):
        fila.append(self.matriza[i][j]+self.matrizb[i][j])
      c.append(fila)
    return c

if __name__ == "__main__":
  pass
         