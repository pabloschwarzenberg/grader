import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))
        
        if len(posiciones_vacias) > 0:
            fila, columna = self.mejorJugada()
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def mejorJugada(self):
        mejor_jugada = None
        mejor_puntaje = float('-inf')

        for fila, columna in self.obtenerPosicionesVacias():
            self.tablero[fila][columna] = self.raton
            puntaje = self.minimax(0, False)
            self.tablero[fila][columna] = 0

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_jugada = (fila, columna)
        
        return mejor_jugada

    def minimax(self, profundidad, es_maximizador):
        estado = self.indicarEstado()
        if estado != 0:
            return estado

        if es_maximizador:
            mejor_puntaje = float('-inf')
            for fila, columna in self.obtenerPosicionesVacias():
                self.tablero[fila][columna] = self.raton
                puntaje = self.minimax(profundidad + 1, False)
                self.tablero[fila][columna] = 0
                mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for fila, columna in self.obtenerPosicionesVacias():
                self.tablero[fila][columna] = self.gato
                puntaje = self.minimax(profundidad + 1, True)
                self.tablero[fila][columna] = 0
                mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def obtenerPosicionesVacias(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))
        return posiciones_vacias

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return self.tablero[i][0]
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return self.tablero[0][i]
        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return self.tablero[0][2]
        
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return 0
        
        return 1

# Ejemplo de uso
juego = JuegoDelGato()

while True:
    print("=== Juego del Gato ===")
    print("Tablero:")
    tablero = juego.mostrar_tablero()
    for fila in tablero:
        print(fila)
    print()

    # Turno del jugador
    fila = int(input("Ingresa la fila (0-2): "))
    columna = int(input("Ingresa la columna (0-2): "))

    if not juego.jugarGato(fila, columna):
        print("Movimiento inválido. Inténtalo de nuevo.")
        continue
    
    estado = juego.indicarEstado()
    if estado == 1:
        print("¡Empate!")
        break
    elif estado == 2:
        print("¡Has ganado!")
        break

    # Turno del ratón
    print("Turno del ratón...")
    if not juego.jugarRaton():
        print("El ratón no pudo realizar una jugada. Fin del juego.")
        break
    
    estado = juego.indicarEstado()
    if estado == 1:
        print("¡Empate!")
        break
    elif estado == -1:
        print("¡El ratón ha ganado!")
        break
