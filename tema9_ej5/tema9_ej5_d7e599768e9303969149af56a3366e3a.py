class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Tablero vacío
        self.turno_gato = True  # True si es el turno del gato, False si es el turno del ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1  # Asignar posición al gato
            self.turno_gato = False  # Cambiar turno al ratón
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
            fila, columna = posiciones_vacias[0]  # Estrategia simple: elegir la primera posición vacía
            self.tablero[fila][columna] = -1  # Asignar posición al ratón
            self.turno_gato = True  # Cambiar turno al gato
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobar si hay ganador en filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:  # Gato gana
                return 2
            elif fila == [-1, -1, -1]:  # Ratón gana
                return 3
        
        # Comprobar si hay ganador en columnas
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna == [1, 1, 1]:  # Gato gana
                return 2
            elif columna == [-1, -1, -1]:  # Ratón gana
                return 3
        
        # Comprobar si hay ganador en diagonales
        diagonal1 = [self.tablero[i][i] for i in range(3)]
        diagonal2 = [self.tablero[i][2-i] for i in range(3)]
        if diagonal1 == [1, 1, 1] or diagonal2 == [1, 1, 1]:  # Gato gana
            return 2
        elif diagonal1 == [-1, -1, -1] or diagonal2 == [-1, -1, -1]:  # Ratón gana
            return 3
        
        # Comprobar si hay empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1  # Empate
        
        # No hay ganador ni empate, se puede seguir jugando
        return 0


# Código para probar el juego
if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego.mostrar_tablero())
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego.mostrar_tablero())
