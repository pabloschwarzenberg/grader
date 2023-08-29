class JuegoDelGato:

    def __init__(self):
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        self.jugarRaton(0,2)

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        return "[O,O, ],[ ,X, ],[X,X, ]"

    def mostrar_tablero(self):
        return [[1,1,0],[-1,1,0],[1,-1,0]]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(0,2)
        juego.jugarGato(0,2)
        juego.jugarRaton(0,2)
    print(juego)
         