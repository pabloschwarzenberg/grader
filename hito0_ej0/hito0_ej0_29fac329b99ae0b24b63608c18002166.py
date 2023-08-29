def pintar_region(tablero, pos,  color_nuevo):
    color_actual = tablero[pos[1]][pos[0]]
    if color_actual == color_nuevo:
        return
    tablero[pos[1]][pos[0]] = color_nuevo
    coordenadas_con_color_antiguo = []
    for i in range(-1,2):
        if pos[1] + i >= 0 and pos[1] + i < len(tablero) and tablero[pos[1] + i][pos[0]] == color_actual:
            coordenadas_con_color_antiguo.append([pos[0],pos[1] + i])
        if pos[0] + i >= 0 and pos[0] + i < len(tablero) and tablero[pos[1]][pos[0] + i] == color_actual:
            coordenadas_con_color_antiguo.append([pos[0] + i, pos[1]])
    if len(coordenadas_con_color_antiguo) == 0:
        return
    else:
        for elem in coordenadas_con_color_antiguo:
            pintar_region(tablero, elem, color_nuevo)

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
      