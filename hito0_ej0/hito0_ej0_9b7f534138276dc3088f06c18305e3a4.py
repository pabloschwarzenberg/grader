def pintar_region(tablero, pos,  color_nuevo):
    color_antiguo=tablero[pos[0]][pos[1]]
    if tablero[pos[0]][pos[1]]==color_antiguo:
        tablero[pos[0]][pos[1]]=color_nuevo
    else:
                return
    if pos[0]>0:
        nueva_pos=(pos[0]-1,pos[1])
        pintar_region(tablero,nueva_pos,color_nuevo)
    if pos[0]<len(tablero)-1:
        nueva_pos=(pos[0]+1,pos[1])
        pintar_region(tablero,nueva_pos,color_nuevo)
    if pos[1]>0:
        nueva_pos=(pos[0],pos[1]-1)
        pintar_region(tablero,nueva_pos,color_nuevo)
    if pos[1]<len(pos[0])-1:
        nueva_pos=(pos[0],pos[1]+1)
        pintar_region(tablero,nueva_pos,color_nuevo)
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
      