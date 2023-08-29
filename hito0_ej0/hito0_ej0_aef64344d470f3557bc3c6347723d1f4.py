def pintar_region(tablero,pos,color_nuevo):
    print(pos)
    if tablero[pos[0]][pos[1]]==color_nuevo or tablero[pos[0]][pos[1]]==1:
        return
    elif pos[0]==(len(tablero)-1) or pos[1]==(len(tablero)-1) or pos[0]==-1 or pos[1]==-1:
        tablero[pos[0]][pos[1]]=color_nuevo
        return
    else:
        tablero[pos[0]][pos[1]]=color_nuevo
        return pintar_region(tablero,[pos[0],pos[1]+1],color_nuevo),pintar_region(tablero,[pos[0],pos[1]-1],color_nuevo),pintar_region(tablero,[pos[0]+1,pos[1]],color_nuevo),pintar_region(tablero,[pos[0]-1,pos[1]],color_nuevo)
    


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
      