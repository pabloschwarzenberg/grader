class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        return ""

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        return False

    def jugarRaton(self):
        tab = self.tablero
        for i in range(3):
            for j in range(3):
                if tab[i][j] == 0:
                    tab[i][j] = -1
                    return True

        return False

    def indicarEstado(self):
        tab = self.tablero
        for k in range(3):
            contador1 = 0
            contador2 = 0
            for l in range(3):
                if tab[k][l] == 1:
                    contador1 += 1
                if tab[k][l] == -1:
                    contador2 += 1
        if contador1 == 3:
            return 2

        if contador2 == 3:
            return 3

        for i in range(3):
            contador1 = 0
            contador2 = 0
            for j in range(3):
                if tab[j][i] == 1:
                    contador1 += 1
                if tab[j][i] == -1:
                    contador2 += 1

        if contador1 == 3:
            return 2

        if contador2 == 3:
            return 3

        if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2]:
            if tab[0][0] == 1:
                return 2
            if tab[0][0] == -1:
                return 3

        if tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0]:
            if tab[0][2] == 1:
                return 2
            if tab[0][2] == -1:
                return 3

        check = False
        for m in range(3):
            for n in range(3):
                if tab[m][n] == 0:
                    check = True
        if check:
            return 0
        return 1

    def cargar_tablero(self, tablero):
        self.tablero = tablero

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