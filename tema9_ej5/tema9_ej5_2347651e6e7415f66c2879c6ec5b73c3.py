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
        movimientos = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos.append((fila, columna))

        if len(movimientos) > 0:
           
            if (0, 0) in movimientos:
                movimiento_elegido = (0, 0)
            else:
                movimiento_elegido = movimientos[0]

            fila, columna = movimiento_elegido
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz
        else:
            raise ValueError("La matriz debe ser de tamaño 3x3.")

    def indicarEstado(self):
        ganador = 0
        empate = True

        # Comprobación de filas
        for fila in range(3):
            if abs(sum(self.tablero[fila])) == 3:
                ganador = 2 if sum(self.tablero[fila]) == 3 else 3
                empate = False

       
        for columna in range(3):
            if abs(sum(row[columna] for row in self.tablero)) == 3:
                ganador = 2 if sum(row[columna] for row in self.tablero) == 3 else 3
                empate = False

      
        diagonal_principal = [self.tablero[i][i] for i in range(3)]
        diagonal_secundaria = [self.tablero[i][2 - i] for i in range(3)]
        if abs(sum(diagonal_principal)) == 3 or abs(sum(diagonal_secundaria)) == 3:
            if sum(diagonal_principal) == 3 or sum(diagonal_secundaria) == 3:
                ganador = 2
            else:
                ganador = 3
            empate = False

        if empate:
            return 1  
        elif ganador != 0:
            return ganador  
        else:
            return 0  
         