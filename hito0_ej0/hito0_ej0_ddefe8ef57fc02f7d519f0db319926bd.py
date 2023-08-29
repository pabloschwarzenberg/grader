def pintar_region(tablero, pos, color_nuevo, color_ant = ""):
    largo = len(tablero[0])
    ancho = len(tablero)
    if color_ant == "":
        color_ant = tablero[pos[0]][pos[1]]
    tablero[pos[0]][pos[1]] = color_nuevo
    if pos[0] - 1 > -1 and [pos[0] - 1, pos[1]] != color_nuevo and tablero[pos[0] - 1][pos[1]] == color_ant:
        pintar_region(tablero, [pos[0] - 1, pos[1]], color_nuevo, color_ant)
    if pos[0] + 1 < ancho and [pos[0] + 1, pos[1]] != color_nuevo and tablero[pos[0] + 1][pos[1]] == color_ant:
        pintar_region(tablero, [pos[0] + 1, pos[1]], color_nuevo, color_ant)
    if pos[1] - 1 > -1 and [pos[0], pos[1] - 1] != color_nuevo and tablero[pos[0]][pos[1] - 1] == color_ant:
        pintar_region(tablero, [pos[0], pos[1] - 1], color_nuevo, color_ant)
    if pos[1] + 1 < largo and [pos[0], pos[1] + 1] != color_nuevo and tablero[pos[0]][pos[1] + 1] == color_ant:
        pintar_region(tablero, [pos[0], pos[1] + 1], color_nuevo, color_ant)

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
      