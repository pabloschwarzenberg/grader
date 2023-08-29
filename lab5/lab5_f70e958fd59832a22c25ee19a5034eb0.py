def revisar_horizontal(tablero,fila):
  raton=0
  gato=0
  for i in range(0,3):
   if (tablero[fila][i]=='O'):
     raton=raton+1
   if (tablero[fila][i]=='X'):
     gato=gato+1
  if (raton==3):
    return(1)
  if(gato==3):
    return(-1)
  else:
     return(0)
        

def revisar_vertical(tablero,columna):
  gato=0
  raton=0
  for i in range(0,3):
    if(tablero[i][columna]=='O'):
      raton=raton+1
    if(tablero[i][columna]=='X'):
      gato=gato+1
  if(raton==3):
    return(1)
  if(gato==3):
    return(-1)
  else:
    return(0)
    
def revisar_diagonal_derecha(tablero):
   gato=0
   raton=0
   for i in range(0,3):
     for j in range (0,3):
       if(i==j):
         if(tablero[i][j]=='O'):
            raton=raton+1
         if(tablero[i][j]=='X'):
            gato=gato+1
   if(raton==3):
     return(1)
   if(gato==3):
     return(-1)
   else:
     return(0)
 
def revisar_diagonal_izquierda(tablero):
   gato=0
   raton=0
   for i in range(0,3):
     for j in range(0,3):
       if(i+j==2):
         if(tablero[i][j]=='O'):
           raton=raton+1
         if(tablero[i][j]=='X'):
           gato=gato+1
   if(raton==3):
     return(1)
   if(gato==3):
     return(-1)
   else:
     return(0)
    
      
      