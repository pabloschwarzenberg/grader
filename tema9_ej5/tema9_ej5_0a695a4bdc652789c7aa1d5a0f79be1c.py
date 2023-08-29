import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False

    def jugarRaton(self):
        # Lógica para la jugada del ratón (puedes implementarla según tu criterio)
        # Aquí se muestra un ejemplo básico de la jugada del ratón que elige una celda vacía al azar
        celdas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    celdas_vacias.append((i, j))
        if celdas_vacias:
            fila, columna = random.choice(celdas_vacias)
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Lógica para verificar el estado del juego (puedes implementarla según tus reglas)
        # Aquí se muestra un ejemplo básico que siempre retorna 0 (el juego no ha terminado)
        return 0


# Ejemplo de uso
juego = JuegoDelGato()
print(juego.mostrar_tablero())  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
juego.jugarGato(1, 1)
print(juego.mostrar_tablero())  # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
juego.jugarRaton()
print(juego.mostrar_tablero())  # [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
