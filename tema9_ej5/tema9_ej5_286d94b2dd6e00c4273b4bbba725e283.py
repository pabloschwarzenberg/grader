class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        return False

    def jugarRaton(self):
        # Obtener la jugada más inteligente del ratón
        fila, columna = self.obtenerJugadaInteligente()

        if fila is not None and columna is not None:
            self.tablero[fila][columna] = -1
            return True
        return False

    def obtenerJugadaInteligente(self):
        # Implementa aquí la lógica para obtener la jugada más inteligente del ratón
        # En este ejemplo, se escoge la primera celda vacía disponible en orden de izquierda a derecha y de arriba a abajo
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return i, j
        return None, None

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) != 3 or any(len(row) != 3 for row in matriz):
            print("La matriz debe tener dimensiones de 3x3")
            return
        self.tablero = matriz

    def indicarEstado(self):
        # Revisa todas las posibles combinaciones de victoria
        combinaciones_victoria = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for combinacion in combinaciones_victoria:
            fila1, columna1 = combinacion[0]
            fila2, columna2 = combinacion[1]
            fila3, columna3 = combinacion[2]

            if (
                self.tablero[fila1][columna1] == self.tablero[fila2][columna2]
                == self.tablero[fila3][columna3]
            ):
                if self.tablero[fila1][columna1] == 1:
                    return 2  # Ganó el gato
                elif self.tablero[fila1][columna1] == -1:
                    return 3  # Ganó el ratón

        # Si no hay ganador, se verifica si hay empate o si se puede seguir jugando
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  # Empate
        return 0  # Se puede seguir jugando


# Ejemplo
