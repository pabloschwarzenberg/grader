import random
class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] != 0:
            return False
        else:
            self.tablero[fila][columna] = -1
            return True
        pass

    def jugarRaton(self):
        fila = random.randint(0,2)
        columna = random.randint(0,2)
        if self.tablero[fila][columna] != 0:
            return False
        else:
            self.tablero[fila][columna] = 1
            return True
        pass

    def indicarEstado(self):
        i = 0
        j = 0
        while i < 3:
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == 1:
                print('gana raton')
                return 3
            elif self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == -1:
                print('gana gato')
                return 2
            i += 1
            if i == 3:
                return 0

        while j < 3:
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] == 1:
                return 3
            elif self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] == -1:
                return 2
            j += 1
            if j == 3:
                return 0

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 3
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 2
        else:
            return 0

        pass

    def cargar_tablero(self,tablero):
        pass

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(fila)
            return [1,2]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
        juego.mostrar_tablero()
    print(juego)
         