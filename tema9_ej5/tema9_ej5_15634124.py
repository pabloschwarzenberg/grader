class JuegoDelGato:

    def __init__(self):
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==-1 or self.tablero[fila][columna]==1:
            return False
        if self.tablero[fila][columna]==0:
           self.tablero[fila][columna]==1
           return True

    def jugarRaton(self):
        tablero_opcion=self.talbero
        for i in range(len(tablero_opcion)):
            for j in range(len(tablero_opcion)):
                a=tablero_opcion[i][j]
                if a== 1:
                   break
            for j in range(len(tablero_opcion)):
                a=tablero_opcion[i][j]
                if a== -1:
                  continue
                if a ==0:
                    a=-1
                
                
               
               
               
            
            
        

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        pass

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
         