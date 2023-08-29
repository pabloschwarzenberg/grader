class JuegoDelGato:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
    
    def jugarGato(self, fila, columna):
        if self.board[fila][columna] == 0:
            self.board[fila][columna] = 1
            return True
        return False

    def jugarRaton(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.board

    def cargar_tablero(self, matriz):
        self.board = matriz

    def check_winner(self):
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                return self.board[i][0]
            if abs(sum(self.board[j][i] for j in range(3))) == 3:
                return self.board[0][i]

        if abs(sum(self.board[i][i] for i in range(3))) == 3:
            return self.board[0][0]
        if abs(sum(self.board[i][2-i] for i in range(3))) == 3:
            return self.board[0][2]

        return 0

    def indicarEstado(self):
        winner = self.check_winner()
        if winner != 0:
            return 2 if winner == 1 else 3
        
        if any(0 in row for row in self.board):
            return 0  # Hay celdas vacías, el juego continúa

        return 1  # No hay celdas vacías, es un empate
