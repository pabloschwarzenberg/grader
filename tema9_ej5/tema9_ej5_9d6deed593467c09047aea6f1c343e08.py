class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turnoGato = True
        self.jugadasRealizadas = 0
        
    def jugarGato(self, fila, columna):
        if self.jugadaPosible(fila, columna):
            self.tablero[fila][columna] = 1
            self.turnoGato = False
            self.jugadasRealizadas += 1
            return True
        else:
            return False

    def jugarRaton(self):
        mejorJugada = self.encontrarMejorJugada(-1) # -1 representa al ratón
        if mejorJugada is None:
            return False
        else:
            fila, columna = mejorJugada
            self.tablero[fila][columna] = -1
            self.turnoGato = True
            self.jugadasRealizadas += 1
            return True

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        if self.hayGanador(1): # ganó el gato
            return 2
        elif self.hayGanador(-1): # ganó el ratón
            return 3
        elif self.tableroCompleto(): # empate
            return 1
        else: # se puede seguir jugando
            return 0

    def tableroCompleto(self):
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    return False
        return True

    def hayGanador(self, jugador):
        for i in range(3):
            # revisar filas
            if self.tablero[i][0] == jugador and self.tablero[i][1] == jugador and self.tablero[i][2] == jugador:
                return True
            # revisar columnas
            if self.tablero[0][i] == jugador and self.tablero[1][i] == jugador and self.tablero[2][i] == jugador:
                return True
        # revisar diagonales
        if self.tablero[0][0] == jugador and self.tablero[1][1] == jugador and self.tablero[2][2] == jugador:
            return True
        if self.tablero[0][2] == jugador and self.tablero[1][1] == jugador and self.tablero[2][0] == jugador:
            return True
        return False

    def jugadaPosible(self, fila, columna):
        return self.tablero[fila][columna] == 0

    def encontrarMejorJugada(self, jugador):
        mejorJugada = None
        mejorPuntaje = float("-inf")
        for i in range(3):
            for j in range(3):
                if self.jugadaPosible(i, j):
                    self.tablero[i][j] = jugador # simular jugada
                    puntaje = self.evaluarTablero(jugador)
                    self.tablero[i][j] = 0 # deshacer jugada
                    if puntaje > mejorPuntaje:
                        mejorPuntaje = puntaje
                        mejorJugada = (i, j)
        return mejorJugada

    def evaluarTablero(self, jugador):
        if self.hayGanador(jugador):
            return 1
        elif self.tableroCompleto():
            return 0
        else:
            puntaje = 0
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == jugador:
                        puntaje += 1
                    elif self.tablero[i][j] == -jugador:
                        puntaje -= 1
            return puntaje
        