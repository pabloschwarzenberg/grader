def vecinos(tablero,pos):
        lista=[]
        if (pos[0]-1)>=0 and (pos[1]-1)>=0:
                lista.append([pos[0]-1,pos[1]-1])
        if (pos[0]-1)>=0 and (pos[1])>=0:
                lista.append([pos[0]-1,pos[1]])
        if (pos[0]-1)>=0 and (pos[1]+1)>=0:
                lista.append([pos[0]-1,pos[1]+1])
        if (pos[0])>=0 and (pos[1]-1)>=0:
                lista.append([pos[0],pos[1]-1])
        if (pos[0])>=0 and (pos[1]+1)>=0:
                lista.append([pos[0],pos[1]+1])
        if (pos[0]+1)>=0 and (pos[1]-1)>=0:
                lista.append([pos[0]+1,pos[1]-1])
        if (pos[0]+1)>=0 and (pos[1])>=0:
                lista.append([pos[0]+1,pos[1]])
        if (pos[0]+1)>=0 and (pos[1]+1)>=0:
                lista.append([pos[0]+1,pos[1]+1])
        
        return lista

def pintar_region(tablero, pos,  color_nuevo):
        if tablero[pos[0]][pos[1]]!=0:
                return
        tablero[pos[0]][pos[1]]=color_nuevo
        for i in vecinos(tablero,pos):
                        pintar_region(tablero,i,color_nuevo)

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
      