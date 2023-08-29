class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.turno_gato = True
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1 
            self.turno_gato = False 
            return True
        else:
            return False
    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))
        if posiciones_vacias:
            fila, columna = posiciones_vacias[0] 
            self.tablero[fila][columna] = -1  
            self.turno_gato = True 
            return True
        else:
            return False
    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2
            elif fila == [-1, -1, -1]:
                return 3
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna == [1, 1, 1]:
                return 2
            elif columna == [-1, -1, -1]:
                return 3
        diagonal1 = [self.tablero[i][i] for i in range(3)]
        diagonal2 = [self.tablero[i][2-i] for i in range(3)]
        if diagonal1 == [1, 1, 1] or diagonal2 == [1, 1, 1]: 
            return 2
        elif diagonal1 == [-1, -1, -1] or diagonal2 == [-1, -1, -1]:
            return 3
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1 
        return 0

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego.mostrar_tablero())
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego.mostrar_tablero())