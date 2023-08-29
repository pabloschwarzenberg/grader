class JuegodelGato:
  def __init__(self):
    self.tablero=[[0,0,0]
                  [0,0,0]
                  [0,0,0]]
  def mostrar_tablero(self):
    for i in range(len(self.tablero)):
      for j in range(len(self.tablero)):
        posicion=self.tablero[i][j]
        if posicion == 0:
          posicion="celda vacía"
         if posicion == 1:
           posicion = "gato"
         if posicion == -1:
           posicion = "ratón"
    return posicion
  
  def jugarGato(self,fila,columna):
    if self.tablero[fila][columna] == 0
      return True
    else:
      return False
  
  def jugarRaton(self,fila,columna):
    if self.tablero[fila][columna] == 0:
      return True
    if self.tablero[fila][columna] == 0:
      return False
  
  def cargar_tablero(self,matriz):
    matriz=mostrar_tablero(self)
  
  def tiene_fila(self,f):
    tiene=((self.tablero[f][0] == 1 or -1 and
           (self.tablero[f][1] == 1 or -1 and
           (self.tablero[f][2] == 1 or -1 ))
    return tiene 
  
  def tiene_columna (self,c):
    tiene = ((self.tablero[0][c] == (1 or -1) and
             (self.tablero[1][c] == (1 or -1) and
             (self.tablero[2][c] == (1 or -1)))
    return tiene 
    
  def tiene_diagonal (self)
    tiene_diagonal=((self.tablero[0][0] == (1 or -1) and
                    (self.tablero[1][1] == (1 or -1) and
                    (self.tablero[2][2] == (1 or -1)))
    tiene_antidiagonal = ((self.tablero[2][2] == (1 or -1) and
                          (self.tablero[1][1] == (1 or -1) and
                          (self.tablero[2][0] == (1 or -1)))
    tiene= tiene_diagonal or tiene_antidiagonal
    return tiene 
    
  def ganador(self):
    ganador=((self.tiene_fila(0,1) or
            (self.tiene_fila (1,1) or
            (self.tiene_fila (2,1) or
            (self.tiene_columna(0,1) or
            (self.tiene_columna(0,2) or
            (self.tiene_columna(0,3) or
            (self.tiene_diagonal(1))