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
        
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    score = self.minimax(False)
                    self.tablero[i][j] = 0

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            self.tablero[best_move[0]][best_move[1]] = -1
            return True
        else:
            return False

    def minimax(self, is_maximizing):
        result = self.indicarEstado()

        if result != 0:
            return self.get_score(result)

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        score = self.minimax(False)
                        self.tablero[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        score = self.minimax(True)
                        self.tablero[i][j] = 0
                        best_score = min(score, best_score)
            return best_score

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        
        for fila in self.tablero:
            if fila.count(1) == 3:
                return 2  
            elif fila.count(-1) == 3:
                return 3  

        
        for i in range(3):
            columna = [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]]
            if columna.count(1) == 3:
                return 2  
            elif columna.count(-1) == 3:
                return 3  

        
        diagonal1 = [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]]
        diagonal2 = [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]]
        if diagonal1.count(1) == 3 or diagonal2.count(1) == 3:
            return 2  
        elif diagonal1.count(-1) == 3 or diagonal2.count(-1) == 3:
            return 3  

        
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  

        
        return 0

    def get_score(self, result):
        if result == 1:
            return 0  
        elif result == 2:
            return 1  
        elif result == 3:
            return -1 
         