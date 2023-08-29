def pintar_region(tablero,pos,color_nuevo):
    x=pos[0]
    y=pos[1]
    color=tablero[y][x]
    tablero[y][x]=color_nuevo
    try:
        if tablero[y+1][x]==color:   #2do condicional evita modularidad->Ej:Pintar de la parte superior a la inferior
            pintar_region(tablero,[x,y+1],color_nuevo)
    except IndexError:
        pass
    try:
        if tablero[y][x+1]==color:
            pintar_region(tablero,[x+1,y],color_nuevo)
    except IndexError:
        pass
    if tablero[y][x-1]==color and x>0:
        pintar_region(tablero,[x-1,y],color_nuevo)
    if tablero[y-1][x]==color and y>0:
        pintar_region(tablero,[x,y-1],color_nuevo)
    return    #Se aprovecha la referencia única a las listas -> Modificación sin retorno

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
      