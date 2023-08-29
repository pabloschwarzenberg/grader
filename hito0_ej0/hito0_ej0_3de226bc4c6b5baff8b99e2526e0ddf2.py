def pintar_region(tablero,pos,color_nuevo):
    x=pos[0]
    y=pos[1]
    if tablero[pos[0]][pos[1]]==0:
        tablero[pos[0]][pos[1]]=color_nuevo
        return True
    elif tablero[pos[0]][pos[1]]==1:
        return False
    
    
    if x < len(tablero)-1 and pintar_region(tablero,[x+1, y],color_nuevo):
        return pintar_region(tablero,[x+1, y],color_nuevo)
    elif y > 0 and pintar_region(tablero,[x, y-1],color_nuevo):
        return pintar_region(tablero,[x, y-1],color_nuevo)
    elif x > 0 and pintar_region(tablero,[x-1, y],color_nuevo):
        return pintar_region(tablero,[x-1, y],color_nuevo)
    elif y < len(grid)-1 and pintar_region(tablero,[x, y+1],color_nuevo):
        return pintar_region(tablero,[x, y+1],color_nuevo)
    else:
        return False
    
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
      