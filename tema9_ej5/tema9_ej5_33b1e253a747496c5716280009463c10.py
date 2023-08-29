import random

class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # El raton debe escoger la jugada más inteligente según el tablero actual, ganando o evitando que el gato gane
        # Si el gato está a punto de ganar, el raton debe evitar que el gato gane
        # Si el gato no puede ganar con el proximo movimiento, el raton debe elegir una jugada que le permita ganar

        # Si el raton no tiene ninguna jugada, elegimos una aleatoria
        mov = None
        cantidad_movimientos_raton = 0
        posibles_movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == -1:
                    cantidad_movimientos_raton += 1
                if self.tablero[i][j] == 0:
                    posibles_movimientos.append([i,j])
        if cantidad_movimientos_raton == 0:
            mov = random.choice(posibles_movimientos)
        else:
            # Primero verificamos si el gato está a punto de ganar
            # Verificamos las filas
            for i in range(3):
                cantidad_gatos = 0
                for j in range(3):
                    if self.tablero[i][j] == 1:
                        cantidad_gatos += 1
                    
                if cantidad_gatos == 2:
                    for j in range(3):
                        if self.tablero[i][j] == 0:
                            mov = [i,j]
                            break
            # Verificamos las columnas
            for j in range(3):
                cantidad_gatos = 0
                for i in range(3):
                    if self.tablero[i][j] == 1:
                        cantidad_gatos += 1
                if cantidad_gatos == 2:
                    for i in range(3):
                        if self.tablero[i][j] == 0:
                            mov = [i,j]
                            break

            # Verificamos las diagonales
            if self.tablero[0][0] == 1 and self.tablero[1][1] == 1 and self.tablero[2][2] == 0:
                mov = [2,2]
            if self.tablero[0][0] == 1 and self.tablero[1][1] == 0 and self.tablero[2][2] == 1:
                mov = [1,1]
            if self.tablero[0][0] == 0 and self.tablero[1][1] == 1 and self.tablero[2][2] == 1:
                mov = [0,0]
            if self.tablero[0][2] == 1 and self.tablero[1][1] == 1 and self.tablero[2][0] == 0:
                mov = [2,0]
            if self.tablero[0][2] == 1 and self.tablero[1][1] == 0 and self.tablero[2][0] == 1:
                mov = [1,1]
            if self.tablero[0][2] == 0 and self.tablero[1][1] == 1 and self.tablero[2][0] == 1:
                mov = [0,2]

            if mov == None:
                for i in range(3):
                    for j in range(3):
                        if self.tablero[i][j] == 0:
                            mov = [i,j]
                            break

        self.tablero[mov[0]][mov[1]] = -1

    def indicarEstado(self):
        # Verificamos el estado del juego, si hay un ganador o si hay un empate o si el juego continua
        # Verificamos las filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] and self.tablero[i][1] == self.tablero[i][2]:
                if self.tablero[i][0] == 1:
                    return 2
                elif self.tablero[i][0] == -1:
                    return 3
        # Verificamos las columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] and self.tablero[1][j] == self.tablero[2][j]:
                if self.tablero[0][j] == 1:
                    return 2
                elif self.tablero[0][j] == -1:
                    return 3
        # Verificamos las diagonales
        if self.tablero[0][0] == self.tablero[1][1] and self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == 1:
                return 2
            elif self.tablero[0][0] == -1:
                return 3
        if self.tablero[0][2] == self.tablero[1][1] and self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == 1:
                return 2
            elif self.tablero[0][2] == -1:
                return 3

        # Verificamos si hay un empate
        cantidad_0 = 0
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    cantidad_0 += 1
        if cantidad_0 == 0:
            return 1
        # Si no hay ganador y no hay empate, el juego continua
        return 0

    def cargar_tablero(self,tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

    def mostrar(self):
        for i in range(3):
            print(self.tablero[i])

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
        juego.mostrar_tablero()
    print(juego)