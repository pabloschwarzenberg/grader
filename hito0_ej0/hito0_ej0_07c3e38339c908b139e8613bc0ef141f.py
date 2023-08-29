def pintar_region(tablero,pos,color_nuevo):
    fila=pos[0]
    columna=pos[1]
    color_original=tablero[fila][columna]
    return pintar(tablero,pos,color_nuevo,color_original)
    

def pintar(tablero,pos,color_nuevo,color_original):
    fila=pos[0]
    columna=pos[1]
    alto=len(tablero)-1
    ancho=len(tablero[0])-1
    color_actual=tablero[fila][columna]
    if color_actual==color_original:
        tablero[fila][columna]=color_nuevo
        for i in range(4):
            if i==0:
                #Avanzar a la derecha
                if columna<ancho:
                    pintar(tablero,[fila,columna+1],color_nuevo,color_original)

            elif i==1:
                #Avanzar a la izquierda
                if columna>0:
                    pintar(tablero,[fila,columna-1],color_nuevo,color_original)

            elif i==2:
		        #Avanzar hacia arriba
                if fila>0:
                    pintar(tablero,[fila-1,columna],color_nuevo,color_original)

            elif i==3:
		        #Avanzar hacia abajo
                if fila<alto:
                    pintar(tablero,[fila+1,columna],color_nuevo,color_original)

        return tablero
    else:
        return

tablero =	       [[1,0,0,0,1,0,1,1],
			[1,1,0,1,1,0,1,0],
			[1,0,0,0,1,0,1,1],
			[1,0,0,1,1,0,1,1],
			[1,1,0,0,1,0,0,0],
			[1,1,1,1,1,0,1,1],
			[0,0,0,0,0,0,0,1],
			[1,1,1,1,1,0,1,1]]

pintar_region(tablero,[1,7],3)
for l in tablero:
	print(l)