class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]

    def _repr_(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        best_move = self.find_best_move()
        if best_move:
            self.tablero[best_move[0]][best_move[1]] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        if self.check_winner(2):
            return 2  # Gato ganó
        elif self.check_winner(-1):
            return 3  # Ratón ganó
        elif self.check_draw():
            return 1  # Empate
        else:
            return 0  # Juego en curso

    def check_winner(self, player):
        # Comprobar filas
        for row in self.tablero:
            if row.count(player) == 3:
                return True

        # Comprobar columnas
        for col in range(3):
            if [self.tablero[row][col] for row in range(3)].count(player) == 3:
                return True

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == player:
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == player:
            return True

        return False

    def check_draw(self):
        for row in self.tablero:
            if 0 in row:
                return False
        return True

    def find_best_move(self):
        best_move = None
        best_score = float("-inf")

        for row in range(3):
            for col in range(3):
                if self.tablero[row][col] == 0:
                    self.tablero[row][col] = -1
                    score = self.minimax(self.tablero, 0, False)
                    self.tablero[row][col] = 0

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        scores = {
            2: 1,   # Gato ganó
            -1: -1,  # Ratón ganó
            0: 0,   # Empate
        }

        result = self.indicarEstado()

        if result != 0:
            return scores[result-1]

        if is_maximizing:
            best_score = float("-inf")
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = 0
                        best_score = max(score, best_score)