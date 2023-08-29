def pintar_region(tablero, pos,  color_nuevo):
	    if tablero pos[0][1] != 1:
        return tablero
      tablero pos[0][1]= color_nuevo
      for posicion in [[1,0], [0,1],[-1,0],[0,-1]]:
        nx = pos[0]+ posicion[0]
        ny = pos[1] + posicion[1]
        if 0 <= nx <= len(tablero[0]):
            if 0 <= ny <= len(tablero):
                tablero = pintar_region(tablero, pos,  color_nuevo)
        
    return tablero

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
      