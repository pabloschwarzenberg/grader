class JuegoDelGato:

    def __init__(self):
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        pass

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        pass

    def mostrar_tablero(self):
        return [[-1,-1,0],[0,1,0],[1,1,0]]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

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
        # Verificar si hay empate
        if all(0 not in fila for fila in self.tablero):
            return 1

        # Verificar si ganó el gato
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2

        # Verificar si ganó el ratón
        for fila in self.tablero:
            if fila == [-1, -1, -1]:
                return 3
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3

        # Si no hay ganador ni empate, el juego sigue
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
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
    estado = juego.indicarEstado()
    if estado == 1:
        print("Empate")
    elif estado == 2:
        print("¡Ganó el gato!")
    elif estado == 3:
        print("¡Ganó el ratón!")
         