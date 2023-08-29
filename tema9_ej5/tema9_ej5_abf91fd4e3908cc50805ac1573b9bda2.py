class JuegoDelGato:

    def __init__(self):
     self.tablero = []
        self.dimension = dimension

        for i in range(dimension):
            # Agrego las filas, cantidad "dimension" de filas.
            self.tablero.append([])
        for i in self.tablero:
            # Por cada fila
            for a in range(dimension):
                # Cada fila le agrego "dimensión" espacios para hacer las columnas.
                i.append(" ")
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        pass

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        pass

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
         