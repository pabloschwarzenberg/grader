def revisar_horizontal(tablero,fila):
    gato=0
    raton=0
    for i in range(0,3):
        if tablero[fila][i]=="X":
            gato=gato+1
        if tablero[fila][i]=="O":
            raton=raton+1
    if gato==3:
        return -1
    if raton==3:
        return 1
    return 0     
 
def revisar_vertical(tablero,columna):
     gato=0
     raton=0
     for i in range(0,3):
         if tablero[i][columna]=="X":
             gato=gato+1
         if tablero[i][columna]=="O":
             raton=raton+1
        
     if gato==3:
       return -1
     if raton==3:
       return 1
     return 0  
    
def revisar_diagonal_derecha(tablero):
     gato=0
     raton=0
     for i in range(0,3):
        if tablero[i][i]=="X":
             gato=gato+1
        if tablero[i][i]=="O":
             raton=raton+1
             
     if gato==3:
       return -1
     if raton==3:
       return 1
     return 0  
         
def revisar_diagonal_izquierda(tablero):
     gato=0
     raton=0
     for i in range(0,3):
        if  tablero[i][2-i]=="X":
              gato=gato+1
        if  tablero[i][2-i]=="O":
              raton=raton+1
     if gato==3:
       return -1
     if raton==3:
       return 1
     return 0  
         