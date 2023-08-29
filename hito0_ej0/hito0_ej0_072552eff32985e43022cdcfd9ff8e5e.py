def pintar_region(tablero, coor, num):
    if coor[0]<0 or coor[0]>=len(tablero) or coor[1]<0 or coor[1]>=len(tablero):
        return
    numero=tablero[coor[0]][coor[1]]
    if numero==1:
        #print(tablero)
        return
    elif numero==0:
        tablero[coor[0]][coor[1]]=num
        for d in [-1,0,1]:
            for c in [-1,0,1]:
                coor[0]+=d
                coor[1]+=c
                pintar_region(tablero,coor,num)
                coor[0]-=d
                coor[1]-=c


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
      