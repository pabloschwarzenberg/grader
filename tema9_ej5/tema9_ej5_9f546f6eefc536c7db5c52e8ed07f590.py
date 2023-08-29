class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))

        if len(movimientos) > 0:
            fila, columna = self.obtenerMejorMovimiento(movimientos)
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def obtenerMejorMovimiento(self, movimientos):
        mejorMovimiento = None
        mejorPuntaje = float('-inf')
        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = self.raton
            puntaje = self.minimax(0, False)
            self.tablero[fila][columna] = 0
            if puntaje > mejorPuntaje:
                mejorPuntaje = puntaje
                mejorMovimiento = movimiento
        return mejorMovimiento

    def minimax(self, profundidad, esMaximizador):
        resultado = self.indicarEstado()
        if resultado != 0:
            return resultado

        if esMaximizador:
            mejorPuntaje = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.raton
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejorPuntaje = max(mejorPuntaje, puntaje)
            return mejorPuntaje
        else:
            mejorPuntaje = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.gato
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejorPuntaje = min(mejorPuntaje, puntaje)
            return mejorPuntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        
        for fila in self.tablero:
            if fila.count(self.gato) == 3:
                return 2  
            elif fila.count(self.raton) == 3:
                return 3  

        
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna.count(self.gato) == 3:
                return 2  
            elif columna.count(self.raton) == 3:
                return 3  

        
        diagonal_principal = [self.tablero[i][i] for i in range(3)]
        diagonal_secundaria = [self.tablero[i][2 - i] for i in range(3)]

        if diagonal_principal.count(self.gato) == 3 or diagonal_secundaria.count(self.gato) == 3:
            return 2  
        elif diagonal_principal.count(self.raton) == 3 or diagonal_secundaria.count(self.raton) == 3:
            return 3  

        
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  

        return 0  


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = map(int, input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(x, y)
        juego.jugarRaton()
    print(juego)
         