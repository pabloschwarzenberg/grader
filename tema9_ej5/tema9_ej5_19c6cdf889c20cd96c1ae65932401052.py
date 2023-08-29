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
        # Lógica para la jugada del ratón más inteligente
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        return False

    def indicarEstado(self):
        # Comprobar si hay ganador en las filas
        for fila in self.tablero:
            if fila.count(1) == 3:
                return 2  # Ganó el gato
            elif fila.count(-1) == 3:
                return 3  # Ganó el ratón

        # Comprobar si hay ganador en las columnas
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna.count(1) == 3:
                return 2  # Ganó el gato
            elif columna.count(-1) == 3:
                return 3  # Ganó el ratón

        # Comprobar si hay ganador en las diagonales
        diagonal1 = [self.tablero[i][i] for i in range(3)]
        diagonal2 = [self.tablero[i][2-i] for i in range(3)]
        if diagonal1.count(1) == 3 or diagonal2.count(1) == 3:
            return 2  # Ganó el gato
        elif diagonal1.count(-1) == 3 or diagonal2.count(-1) == 3:
            return 3  # Ganó el ratón

        # Comprobar si hay empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  # Empate

        # Si no hay ganador ni empate, se puede seguir jugando
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