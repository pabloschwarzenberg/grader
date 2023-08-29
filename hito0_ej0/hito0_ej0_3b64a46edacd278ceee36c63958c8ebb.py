def pintar_region(tablero,pos,color_nuevo,color=None):
	if(color == None):
		color=tablero[pos[0]][pos[1]]
		pos = [0,0]
	if(tablero[pos[0]][pos[1]] == color):
		tablero[pos[0]][pos[1]] = color_nuevo
	if(pos == [len(tablero)-1,len(tablero[0])-1]):
		return
	else:
		if(pos[0] < len(tablero[0])-1):
			pintar_region(tablero,[(pos[0]+1),pos[1]],color_nuevo,color)
		else:
			pintar_region(tablero,[0,(pos[1]+1)],color_nuevo,color)

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
      