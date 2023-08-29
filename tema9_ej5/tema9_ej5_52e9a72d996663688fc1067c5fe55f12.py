class JuegoDelGato:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def playCat(self, row, column):
        if self.board[row][column] == 0:
            self.board[row][column] = 1
            return True
        else:
            return False
    def jugarRaton(self):
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == 0:
                    self.board[row][column] = -1
                    return True
        return False
    def mostrar_tablero(self):
        return self.board
    def cargar_tablero(self, matrix):
        self.board = matrix
    def indicateStatus(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                return self.board[row][0]
            if self.board[0][row] == self.board[1][row] == self.board[2][row] != 0:
                return self.board[0][row]
            if self.board[row][0] == self.board[1][1] == self.board[2][2] != 0:
                return self.board[row][0]
            if self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
                return self.board[2][0]
        if 0 not in self.board:
            return 1
        return 0
