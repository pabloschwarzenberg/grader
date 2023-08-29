def pintar_region(tablero,x,n):
    numero =tablero[x[0]][x[1]]
    opciones=[-1,0,1]
    if numero==1:
        return 
    if numero==0:
        (tablero[x[0]])[x[1]]=n
        for d in opciones:
            for c in opciones:
                x[0]+=d
                x[1]+=c
                if 0<=x[0]<len(tablero) and 0<=x[1]<len(tablero[0]):
                    pintar_region(tablero,x,n)
                x[0]-=d
                x[1]-=c

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
      