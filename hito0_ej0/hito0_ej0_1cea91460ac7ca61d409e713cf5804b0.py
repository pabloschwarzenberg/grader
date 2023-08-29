#se consideraron las diferentes casillas a partir del 0
def pintar_region(tablero,pos,color_nuevo,color_anterior):
    #print(pos)
    fila=pos[0]
    col=pos[1]
    try:
        tablero[fila][col]
        if fila<0 or col<0:return 
    except IndexError:
        return
    if tablero[fila][col]!=color_anterior:
        return
    else:
        tablero[fila][col]=color_nuevo

    mov=["abajo","izquierda","arriba","derecha"]
    for accion in mov:
        if accion=="arriba":
            pintar_region(tablero,[fila-1,col],color_nuevo,color_anterior)
        if accion=="derecha":
            pintar_region(tablero,[fila,col+1],color_nuevo,color_anterior)
        if accion=="abajo":
            pintar_region(tablero,[fila+1,col],color_nuevo,color_anterior)
        if accion=="izquierda":
            pintar_region(tablero,[fila,col-1],color_nuevo,color_anterior)
            
  

def color_casilla(tablero,fila,col):
    color=tablero[fila][col]
    return color
    
  
    
    

tablero =	       [[1,0,0,0,1,0,1,1],
			[1,1,0,1,1,0,1,0],
			[1,0,0,0,1,0,1,1],
			[1,0,0,1,1,0,1,1],
			[1,1,0,0,1,0,0,0],
			[1,1,1,1,1,0,1,1],
			[0,0,0,0,0,0,0,1],
			[1,1,1,1,1,0,1,1]]
        
pintar_region(tablero,[3,2],3,color_casilla(tablero,3,2))
for l in tablero:
	print(l)

print("-----------------------------")
pintar_region(tablero,[4,5],2,color_casilla(tablero,4,5))
for j in tablero:
	print(j)

print("-----------------------------")
pintar_region(tablero,[1,6],6,color_casilla(tablero,1,6))
for k in tablero:
	print(k)




