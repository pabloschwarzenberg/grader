class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0 for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    s += " "
                elif celda == 1:
                    s += "X"
                elif celda == -1:
                    s += "O"
                s += "|"
            s = s[:-1]
            s += "\n"
        return s

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Comprobar si el ratón puede ganar en el siguiente movimiento
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    if self.indicarEstado() == 3:
                        return True
                    else:
                        self.tablero[i][j] = 0

        # Comprobar si el gato puede ganar en el siguiente movimiento y bloquearlo
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = 1
                    if self.indicarEstado() == 2:
                        self.tablero[i][j] = -1
                        return True
                    else:
                        self.tablero[i][j] = 0

        # Jugar en el centro si está disponible
        if self.tablero[1][1] == 0:
            self.tablero[1][1] = -1
            return True

        # Jugar en una esquina si está disponible
        esquinas = [(0,0), (0,2), (2,0), (2,2)]
        for i,j in esquinas:
            if self.tablero[i][j] == 0:
                self.tablero[i][j] = -1
                return True

        # Jugar en cualquier lado disponible
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True

        # No hay jugadas disponibles
        return False

    def indicarEstado(self):
        # Comprobar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2]:
                if fila[0] == 1:
                    return 2
                elif fila[0] == -1:
                    return 3

        # Comprobar columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j]:
                if self.tablero[0][j] == 1:
                    return 2
                elif self.tablero[0][j] == -1:
                    return 3

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == 1:
                return 2
            elif self.tablero[0][0] == -1:
                return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == 1:
                return 2
            elif self.tablero[0][2] == -1:
                return 3

        # Comprobar si hay celdas vacías
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    return 0

        # Empate
        return 1

    def cargar_tablero(self,tablero):
        for i in range(3):
            for j in range(3):
                self.tablero[i][j]=tablero[i][j]

    def mostrar_tablero(self):
        return [[celda for celda in fila] for fila in self.tablero]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         