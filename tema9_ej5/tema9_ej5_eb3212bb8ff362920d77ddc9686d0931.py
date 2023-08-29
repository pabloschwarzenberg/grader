import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False
    
    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))
        
        if len(posiciones_vacias) == 0:
            return False
        
        fila, columna = self.mejorJugada(posiciones_vacias, -1)
        self.tablero[fila][columna] = -1
        return True
    
    def mejorJugada(self, posiciones, jugador):
        mejor_jugada = None
        mejor_puntaje = -float('inf')
        
        for fila, columna in posiciones:
            self.tablero[fila][columna] = jugador
            puntaje = self.minimax(jugador)
            self.tablero[fila][columna] = 0
            
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_jugada = (fila, columna)
        
        return mejor_jugada
    
    def minimax(self, jugador):
        estado = self.indicarEstado()
        
        if estado == 2:
            return 1
        elif estado == 3:
            return -1
        elif estado == 1:
            return 0
        
        if jugador == -1:
            mejor_puntaje = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = jugador
                        puntaje = self.minimax(1)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = jugador
                        puntaje = self.minimax(-1)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            return False
        self.tablero = matriz
        return True
    
    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón
        
        # Verificar si hay un ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón
        
        # Verificar si hay un ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón
        
        # Si no hay ganador, verificar si hay empate o se puede seguir jugando
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  # Empate
        else:
            return 0  # Juego en progreso

# Ejemplo de uso
juego = JuegoDelGato()
juego.cargar_tablero([["O", "O", ""], ["", "X", ""], ["X", "X", ""]])
juego.jugarRaton()
print(juego.mostrar_tablero())
print(juego.indicarEstado())
