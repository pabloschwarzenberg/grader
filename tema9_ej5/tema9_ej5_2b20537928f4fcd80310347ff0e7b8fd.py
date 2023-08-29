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
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.jugador_actual = 1
                    return True
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

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3 

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2 
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  

        if all(0 not in fila for fila in self.tablero):
            return 1 

        return 0 


if __name__ == "__main__":
    juego = JuegoDelGato()


    juego.jugarGato(0, 0)  
    juego.jugarRaton() 
    juego.jugarGato(1, 1)  
    juego.jugarRaton()  
    juego.jugarGato(2, 2) 

    tablero = juego.mostrar_tablero()
    for fila in tablero:
        print(fila)

    estado = juego.indicarEstado()
    if estado == 0:
        print("Juego en curso")
    elif estado == 1:
        print("Empate")
    elif estado == 2:
        print("Gato gana")
    elif estado == 3:
        print("Ratón gana")
