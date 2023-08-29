class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False
    
    def jugarRaton(self):
        # Lógica para determinar la jugada más inteligente del ratón
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        return False
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3 or len(matriz[1]) != 3 or len(matriz[2]) != 3:
            raise ValueError("La matriz debe tener dimensiones 3x3")
        
        self.tablero = matriz
    
    def indicarEstado(self):
        # Verificar si hay ganador en filas
        for i in range(3):
            if self.tablero[i][0] != 0 and self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2]:
                return 2 if self.tablero[i][0] == 1 else 3
        
        # Verificar si hay ganador en columnas
        for j in range(3):
            if self.tablero[0][j] != 0 and self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j]:
                return 2 if self.tablero[0][j] == 1 else 3
        
        # Verificar si hay ganador en diagonales
        if self.tablero[0][0] != 0 and self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            return 2 if self.tablero[0][0] == 1 else 3
        
        if self.tablero[2][0] != 0 and self.tablero[2][0] == self.tablero[1][1] == self.tablero[0][2]:
            return 2 if self.tablero[2][0] == 1 else 3
        
        # Verificar si hay empate
        if all(0 not in row for row in self.tablero):
            return 1
        
        # Si no hay ganador ni empate, se puede seguir jugando
        return 0
