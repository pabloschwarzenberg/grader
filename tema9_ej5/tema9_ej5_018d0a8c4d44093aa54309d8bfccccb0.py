class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0],]

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[columna][fila]== 0:
            self.tablero[columna][fila] == 1
            return True, self.tablero
        else:
            return False

    def jugarRaton(self):
        for i in self.tablero:
            for x in i:
                if  x== 0 and i[x-2] == -1 and i[x-1] == -1:
                    i[x]= -1
                    break
                elif x == 0 and i[x-2] == -1 and i[x-1] == -1:
                        i[x] == -1


    def indicarEstado(self):
        for w in self.tablero:
            for f in self.tablero:
                if self.tablero[w][f]==self.tablero[w][f+1]==self.tablero[w][f+2] == 1:
                    return 2

                elif self.tablero[w][f]==self.tablero[w+1][f+1]==self.tablero[w+2][f+2] == 1:
                    return 2
                elif self.tablero[w][f]== self.tablero[w-1][f-1] == self.tablero[w-2][f-2] == 1:
                    return 2

                elif self.tablero[w][f] == self.tablero[w+1][f] == self.tablero[w+2][f] == 1:
                    return 2
                elif self.tablero[w][f] == self.tablero[w][f + 1] == self.tablero[w][f + 2] == -1:
                    return 3

                elif self.tablero[w][f] == self.tablero[w + 1][f + 1] == self.tablero[w + 2][f + 2] == -1:
                    return 3
                elif self.tablero[w][f] == self.tablero[w - 1][f - 1] == self.tablero[w - 2][f - 2] == -1:
                    return 3

                elif self.tablero[w][f] == self.tablero[w + 1][f] == self.tablero[w + 2][f] == -1:
                    return 3


    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         