class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def jugarGato(self,fila,columna):
        if (self.tablero[fila][columna] == 0):
            return True
        elif (self.tablero[fila][columna] == 1 or self.tablero[fila][columna] == -1):
            return False

    def jugarRaton(self):
        return True


    def indicarEstado(self):
    ## Revisar las lineas horizontales

        if (self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2] == 1):
            return 2
        elif (self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2]== 1):
            return 2
        elif (self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2]== 1):
            return 2
    
        ## Revisar las lineas verticales
        elif (self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0]== 1):
            return 2
        elif (self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1]== 1):
            return 2
        elif (self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2]== 1):
            return 2
    
        ## Revisar las lineas diagonales
        elif (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]== 1):
            return 2
        elif (self.tablero[2][0] == self.tablero[1][1] == self.tablero[0][2]== 1):
            return 2
            #raton
        if (self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2] == -1):
            return 2
        elif (self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2]== -1):
            return 2
        elif (self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2]== -1):
            return 2
    
        ## Revisar las lineas verticales
        elif (self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0]== -1):
            return 2
        elif (self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1]== -1):
            return 2
        elif (self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2]== -1):
            return 2
    
        ## Revisar las lineas diagonales
        elif (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]== -1):
            return 2
        elif (self.tablero[2][0] == self.tablero[1][1] == self.tablero[0][2]== -1):
            return 2

        else:
            for fila in self.tablero:
                for columna in fila:
                    if (columna != 0):
                        empate = True
            if empate == True:
                return 1

    def cargar_tablero(self,tablero):
        self.tablero = tablero
        

    def mostrar_tablero(self):
        return [[-1,-1,0],[0,1,0],[1,1,0]]
        
        
if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         