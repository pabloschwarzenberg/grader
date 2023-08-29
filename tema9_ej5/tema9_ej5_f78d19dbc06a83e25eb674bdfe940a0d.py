class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.ganador = 0  # 0: sin ganador, 1: empate, 2: gato gana, 3: ratón gana
        self.turno = 1  # 1: turno del gato, -1: turno del ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.ganador != 0:
            return False

        mejor_jugada = self.obtenerMejorJugada()
        if mejor_jugada:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            self.turno = 1
            return True
        else:
            return False

    def obtenerMejorJugada(self):
        # Implementa aquí tu algoritmo para determinar la jugada más inteligente del ratón
        # Puedes usar cualquier estrategia, como minimax o búsqueda en árbol

        # En esta implementación de ejemplo, simplemente se selecciona la primera celda vacía encontrada
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return i, j
        return None

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz

    def indicarEstado(self):
        if self.ganador == 0:
            if self.hayEmpate():
                return 1
            else:
                return 0
        elif self.ganador == 2:
            return 2
        else:
            return 3

    def hayEmpate(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return False
        return True
