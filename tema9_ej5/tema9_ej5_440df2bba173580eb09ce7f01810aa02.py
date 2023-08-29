class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.gato = 1
        self.raton = -1
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False
    
    def jugarRaton(self):
        # Lógica para la jugada del ratón (estrategia básica)
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    return True
        
        return False
    
    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for fila in self.tablero:
            if fila == [self.gato, self.gato, self.gato]:
                return 2  # Ganó el gato
            if fila == [self.raton, self.raton, self.raton]:
                return 3  # Ganó el ratón
        
        # Verificar si hay un ganador en columnas
        for columna in range(3):
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [self.gato, self.gato, self.gato]:
                return 2  # Ganó el gato
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [self.raton, self.raton, self.raton]:
                return 3  # Ganó el ratón
        
        # Verificar si hay un ganador en diagonales
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [self.gato, self.gato, self.gato] or \
           [self.tablero[2][0], self.tablero[1][1], self.tablero[0][2]] == [self.gato, self.gato, self.gato]:
            return 2  # Ganó el gato
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [self.raton, self.raton, self.raton] or \
           [self.tablero[2][0], self.tablero[1][1], self.tablero[0][2]] == [self.raton, self.raton, self.raton]:
            return 3  # Ganó el ratón
        
        # Verificar si hay empate
        if all(item != 0 for fila in self.tablero for item in fila):
            return 1  # Empate
        
        return 0  # El juego sigue
    
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    
    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.cargar_tablero([[0, 0, -1],
                          [0, 1, 0],
                          [1, 1, 0]])
    
    while juego.indicarEstado() == 0:
        print(juego.mostrar_tablero())
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        
        if juego.indicarEstado() == 0:
            if juego.jugarRaton():
                print("El ratón jugó:")
                print(juego.mostrar_tablero())
            else:
                print("No hay más movimientos posibles para el ratón.")
                break
    
    print(juego.mostrar_tablero())
    estado = juego.indicarEstado()
    
    if estado == 1:
        print("¡Empate!")
    elif estado == 2:
        print("¡Ganó el gato!")
    elif estado == 3:
        print("¡Ganó el ratón!")