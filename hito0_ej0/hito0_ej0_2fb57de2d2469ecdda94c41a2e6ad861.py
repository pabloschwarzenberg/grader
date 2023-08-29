#Grupo Nico
def pintar_region(tablero,pos,color_nuevo):
    try:
        a=tablero[pos[0]][pos[1]]
        if a==0:
            tablero[pos[0]][pos[1]]=color_nuevo
            if tablero[pos[0]+1][pos[1]]==0:
                pintar_region(tablero,[pos[0]+1,pos[1]],color_nuevo)
            if tablero[pos[0]-1][pos[1]]==0:
                pintar_region(tablero,[pos[0]-1,pos[1]],color_nuevo)
            if tablero[pos[0]][pos[1]+1]==0:
                pintar_region(tablero,[pos[0],pos[1]+1],color_nuevo)
            if tablero[pos[0]][pos[1]-1]==0:
                pintar_region(tablero,[pos[0],pos[1]-1],color_nuevo)
            if tablero[pos[0]-1][pos[1]-1]==0:
                pintar_region(tablero,[pos[0]-1,pos[1]-1],color_nuevo)
            if tablero[pos[0]+1][pos[1]+1]==0:
                pintar_region(tablero,[pos[0]+1,pos[1]+1],color_nuevo)
            if tablero[pos[0]+1][pos[1]-1]==0:
                pintar_region(tablero,[pos[0]+1,pos[1]-1],color_nuevo)
            if tablero[pos[0]-1][pos[1]+1]==0:
                pintar_region(tablero,[pos[0]-1,pos[1]+1],color_nuevo)       
    except IndexError:
        pass

tablero =[[1,0,0,0,1,0,1,1],[1,1,0,1,1,0,1,0],[1,0,0,0,1,0,1,1],[1,0,0,1,1,0,1,1],[1,1,0,0,1,0,0,0],[1,1,1,1,1,0,1,1],[0,0,0,0,0,0,0,1],[1,1,1,1,1,0,1,1]]
        

pintar_region(tablero,[3,2],3)

for l in tablero:
    print(l)