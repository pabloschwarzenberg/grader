class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Inicializar tablero vacío
        self.gato = 1  # Representación del gato en el tablero
        self.raton = -1  # Representación del ratón en el tablero

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        if self.indicarEstado() != 0:
            return False
        
        # Buscar la mejor jugada para el ratón
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = self.raton
                    score = self.minimax(0, False)
                    self.tablero[i][j] = 0  # Deshacer jugada
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            self.tablero[best_move[0]][best_move[1]] = self.raton
            return True
        else:
            return False

    def minimax(self, depth, is_maximizing):
        scores = {
            2: 1,   # Gato gana
            3: -1,  # Ratón gana
            1: 0    # Empate
        }
        
        result = self.indicarEstado()
        
        if result != 0:
            return scores[result]
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.gato
                        score = self.minimax(depth + 1, False)
                        self.tablero[i][j] = 0  # Deshacer jugada
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.raton
                        score = self.minimax(depth + 1, True)
                        self.tablero[i][j] = 0  # Deshacer jugada
                        best_score = min(score, best_score)
            return best_score

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay ganador
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == self.gato else 3  # Gato o ratón gana en fila
        
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == self.gato else 3  # Gato o ratón gana en columna
        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3  # Gato o ratón gana en diagonal
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3  # Gato o ratón gana en diagonal
        
        # Verificar si hay empate
        is_full = all(all(cell != 0 for cell in row) for row in self.tablero)
        if is_full:
            return 1  # Empate
        
        # Si no hay ganador ni empate, se puede seguir jugando
        return 0
