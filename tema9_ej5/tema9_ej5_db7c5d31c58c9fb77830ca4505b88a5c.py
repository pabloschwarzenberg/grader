class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Tablero vacío
        self.jugador_actual = 1  # El gato juega primero
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1  # Es el turno del ratón
            return True
        else:
            return False
    
    def jugarRaton(self):
        # Implementa aquí tu estrategia para que el ratón juegue de manera inteligente
        # Puedes utilizar algoritmos de búsqueda o reglas heurísticas
        
        # Aquí, como ejemplo, se elige una casilla vacía al azar
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.jugador_actual = 1  # Es el turno del gato
                    return True
        return False  # No hay casillas vacías, no se puede jugar
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz
    
    def indicarEstado(self):
        # Comprobamos si hay algún ganador en filas, columnas o diagonales
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3
        
        # Si no hay ganador, comprobamos si hay empate o se puede seguir jugando
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  # Empate
        else:
            return 0  # Se puede seguir jugando
         