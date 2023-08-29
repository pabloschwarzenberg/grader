class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.turno = 1  # 1 para el gato, -1 para el ratón

    def __repr__(self):
        repr_str = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    repr_str += " "
                elif celda == 1:
                    repr_str += "X"
                elif celda == -1:
                    repr_str += "O"
            repr_str += "\n"
        return repr_str

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        else:
            return False

    def jugarRaton(self):
        # Estrategia del ratón: jugar en la primera celda vacía que encuentre
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    self.turno = 1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and len(matriz[0]) == 3:
            self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay ganador en las filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay ganador en las columnas
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna == [1, 1, 1]:
                return 2  # Ganó el gato
            elif columna == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay ganador en las diagonales
        diagonal_principal = [self.tablero[i][i] for i in range(3)]
        diagonal_secundaria = [self.tablero[i][2 - i] for i in range(3)]
        if diagonal_principal == [1, 1, 1] or diagonal_secundaria == [1, 1, 1]:
            return 2  # Ganó el gato
        elif diagonal_principal == [-1, -1, -1] or diagonal_secundaria == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Verificar si hay empate
        if all(celda != 0 for fila in self.tablero for celda in fila):
            return 1  # Empate

        # No hay ganador y se puede seguir jugando
        return 0 