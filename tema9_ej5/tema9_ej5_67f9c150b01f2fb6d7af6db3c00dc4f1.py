class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        tablero_str = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == 1:
                    tablero_str += "X "
                elif celda == -1:
                    tablero_str += "O "
                else:
                    tablero_str += "- "
            tablero_str += "\n"
        return tablero_str

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def indicarEstado(self):
        for fila in range(3):
            
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                if self.tablero[fila][0] == 1:
                    return 2  
                else:
                    return 3  
        for columna in range(3):
            
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == 1:
                    return 2 
                else:
                    return 3 
      
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2  
            else:
                return 3  
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == 1:
                return 2  
            else:
                return 3
     
        empate = True
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    empate = False
                    break
            if not empate:
                break
        if empate:
            return 1  
        
        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        if juego.jugarGato(int(x), int(y)):
            juego.jugarRaton()
    print(juego)