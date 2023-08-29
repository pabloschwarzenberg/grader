paint=[]
def pintar_region(tablero, pos, color_nuevo):
    x,y=pos[0],pos[1]
    global paint
    if y+1<8 and tablero[y+1][x]==tablero[y][x]:
        if (y+1,x) not in paint:
            paint.append((y+1,x))
            pintar_region(tablero, [x,y+1], color_nuevo)
    if y-1>-2 and tablero[y-1][x]==tablero[y][x]:
        if (y-1,x) not in paint:
            paint.append((y-1,x))
            pintar_region(tablero, [x,y-1], color_nuevo)
    if x+1<8 and tablero[y][x+1]==tablero[y][x]:
        if (y,x+1) not in paint:
            paint.append((y,x+1))
            pintar_region(tablero, [x+1,y], color_nuevo)
    if x-1>-2 and tablero[y][x-1]==tablero[y][x]:
        if (y,x-1) not in paint:
            paint.append((y,x-1))
            pintar_region(tablero, [x-1,y], color_nuevo)
    else:
        return

tablero =	[[1,0,0,0,1,0,1,1],
			[1,1,0,1,1,0,1,0],
			[1,0,0,0,1,0,1,1],
			[1,0,0,1,1,0,1,1],
			[1,1,0,0,1,0,0,0],
			[1,1,1,1,1,0,1,1],
			[0,0,0,0,0,0,0,1],
			[1,1,1,1,1,0,1,1]]
        
pintar_region(tablero,[3,2],3)
for i,j in paint:
    tablero[i][j]=3
for l in tablero:
	print(l)
      