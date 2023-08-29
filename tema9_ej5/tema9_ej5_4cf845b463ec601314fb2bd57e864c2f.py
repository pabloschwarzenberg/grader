class JuegoDelGato:
  def __init__ (self,fila,columna,matriz):
    self.fila=fila
    self.columna=columna
    self.matriz=matriz
    ################################3
  #def jugarGato(self,fila,columna):
 
  ########################
  #def Raton(self):
##############################  
  def mostrar_tablero(self):
    for fila in range(len(matriz)):
      for columna in range(len(matriz[fila])):
        print(matriz[fila][columna], end="  ")
      print()
    return matriz
  ##############
  def indicarEstado(self):
    terminar=False
    for fila in range(len(matriz)):
      for columna in range(len(matriz[fila])):
        if matriz[fila][columna] in "-":
          terminar = False
        
        elif matriz[fila][columna] in "x" or "o":
          terminar = True
    return terminar
  
