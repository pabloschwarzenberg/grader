def dentro(tablero, pos):
    x = pos[0]
    y = pos[1]
    if x < 0 or y < 0:
        return False
    if x >= len(tablero[0]) or y >= len(tablero):
        return False
    return True

def pintar_region(tablero, pos, color):
    if not dentro(tablero, pos):
        return tablero
    x = pos[0]
    y = pos[1]
    color_original = tablero[y][x]
    tablero[y][x] = color
    for pos2 in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        x2 = x + pos2[0]
        y2 = y + pos2[1]
        if dentro(tablero, (x2, y2)):
            if color_original == tablero[y2][x2]:
                tablero = pintar(tablero, (x2, y2), color)
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
  
def dentro(tablero, pos):
    x = pos[0]
    y = pos[1]
    if x < 0 or y < 0:
        return False
    if x >= len(tablero[0]) or y >= len(tablero):
        return False
    return True



      