class Matriz:
  def __init__(self, celdas=[]):
    self.celdas = celdas

  def __repr__(self):
    s = ""
    for i in range(len(self.celdas)):
      for j in range(len(self.celdas)):
        s += "{0: >5} ".format(self.celdas[i][j])
      s += "\n"
    return s

  def __mul__(self, other):
    for x in range(len(self.celdas)):
      for y in range(len(self.celdas)):
        for z in range(len(self.celdas)):
          print(self.celdas[x][y])
          self.celdas[x][y]=self.celdas[x][y]*other.celdas[x][z]
    return self.celdas


           