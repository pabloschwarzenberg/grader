def pintar_region(tablero, pos,  color_nuevo):
  x = pos[0]
  y = pos[1]
  # tablero[y] es la fila
  # fila[x] es el dato
  color_anterior= tablero[y][x]
  tablero[y][x] = color_nuevo
  
  if y-1>=0:
    if tablero[y-1][x]==color_anterior and tablero[y-1][x]!=color_nuevo:
      pintar_region(tablero,[y-1,x],color_nuevo)
  if x-1>=0:
    if tablero[y][x-1]==color_anterior and tablero[y][x-1]!=color_nuevo:
      pintar_region(tablero,[y,x-1],color_nuevo)
  if y+1<=len(tablero): #largo(numero de filas)
    if tablero[y+1][x]==color_anterior and tablero[y+1][x]!=color_nuevo:
      pintar_region(tablero,[y+1,x],color_nuevo)
  if x+1<=len(tablero[0]):
    if tablero[y][x+1]==color_anterior and tablero[y][x+1]!=color_nuevo :
      pintar_region(tablero,[y,x+1],color_nuevo)
  
  
  

tablero =	[[1,0,0,0,1,0,1,1],
			[1,1,0,1,1,0,1,0],
			[1,0,0,0,1,0,1,1],
			[1,0,0,1,1,0,1,1],
			[1,1,0,0,1,0,0,0],
			[1,1,1,1,1,0,1,1],
			[0,0,0,0,0,0,0,1],
			[1,1,1,1,1,0,1,1]]
        
pintar_region(tablero,[3,2],3)
for l in tablero:
	print(l)
      