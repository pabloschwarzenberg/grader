def pintar_region(tablero, pos,  color_nuevo):
	i=pos[1]
	j=pos[0]
	color_original = tablero[i][j]
	tablero[i][j] = color_nuevo
	if i - 1 >= 0 and tablero[i - 1][j] == color_original:
		pintar_region(tablero, [i-1,j],color_nuevo)
	elif i + 1 >= 0 and tablero[i + 1][j] == color_original:
		pintar_region(tablero, [i+1,j],color_nuevo)
	elif j - 1 >= 0 and tablero[i][j - 1] == color_original:
		pintar_region(tablero, [i,j-1],color_nuevo)
	elif j + 1 >= 0 and tablero[i][j + 1] == color_original:
		pintar_region(tablero, [i,j+1],color_nuevo)
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
      