def pintar(tablero,pos,color) :
    a = pos[0]
    b = pos[1]
    num = tablero[a][b]
    tablero[a][b] = color
    for i in [a-1,a+1] :
        if i >= 0 and i < len(tablero) and tablero[i][b] == num :
            pintar(tablero,[i,b],color)
    for j in [b-1,b+1] :
        if j >= 0 and j < len(tablero) and tablero[a][j] == num :
            pintar(tablero,[a,j],color)

tablero =	[[1,0,0,0,1,0,1,1],
		 [1,1,0,1,1,0,1,0],
		 [1,0,0,0,1,0,1,1],
		 [1,0,0,1,1,0,1,1],
		 [1,1,0,0,1,0,0,0],
		 [1,1,1,1,1,0,1,1],
		 [0,0,0,0,0,0,0,1],
		 [1,1,1,1,1,0,1,1]]
        
pintar(tablero,[3,2],3)
for l in tablero:
	print(l)
