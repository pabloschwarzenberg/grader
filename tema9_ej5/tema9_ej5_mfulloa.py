class JuegoDelGato:
    def __init__(self):
        self.tablero=([0,0,0],[0,0,0],[0,0,0])
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero([fila][columna])==0:
            self.tablero([fila][columna])==1
            return True
        else:
            return False

    def jugarRaton(self):
        pass

    def indicarEstado(self):
        contg=0
        contr=0
        for x in range(len(tablero)):
            for y in range(len(tablero[0])):
                if self.tablero[x][y]==0:
                    return 0
                
    def cargar_tablero(self,tablero):
        self.tablero=tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         
         