class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        t = ""
        for i in self.tablero:
            f = ""
            for j in i:
                if j == 0:
                    f += "  "
                elif j == 1:
                    f += "X "
                else:
                    f += "O "
            t += f + "\n"
        return t

    def jugarGato(self,fila,columna):
        if self.tablero[fila][culumna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for i in range(len(self.tablero)):
            if self.tablero[i].count(-1) == 2 and 0 in self.tablero[i]:
                a = self.tablero[i].index(0)
                self.tablero[i][a] = -1
                return True
            elif i.count(1) == 2 and 0 in i:
                a = self.tablero[i].index(0)
                self.tablero[i][a] = -1
                return True
        for i in range(3):
            l = []
            for j in range(3):
                l.append(self.tablero[j][i])
            if l.count(-1) == 2 and 0 in i:
                self.tablero[i][j] = -1
                return True
            elif i.count(1) == 2 and 0 in i:
                self.tablero[i][j] = -1
                return True
        dd = []
        di = []
        for i in range(3):
            dd.append(self.tablero[i][i])
            di.append(self.tablero[i][2 - i])
        if dd.count(1) == 2 and 0 in i:
            self.tablero[i][i] = -1
            return True
        elif dd.count(-1) == 2 and 0 in i:
            self.tablero[i][i] = -1
            return True
        if di.count(1) == 2 and 0 in i:
            self.tablero[i][i] = -1
            return True
        elif di.count(-1) == 2 and 0 in i:
            self.tablero[i][i] = -1
            return True
        return False

    def indicarEstado(self):
        for i in self.tablero:
            if i.count(-1) == 3:
                return 3
            elif i.count(1) == 3:
                return 2
        for i in range(3):
            l = []
            for j in range(3):
                l.append(self.tablero[j][i])
            if l.count(-1) == 3:
                return 3
            elif l.count(1) == 3:
                return 2
        dd = []
        di = []
        for i in range(3):
            dd.append(self.tablero[i][i])
            di.append(self.tablero[i][2 - i])
        if dd.count(-1) == 3:
            return 3
        elif dd.count(1) == 3:
            return 2
        if di.count(-1) == 3:
            return 3
        elif di.count(1) == 3:
            return 2
        for i in self.tablero:
            if i.count(0)>0:
                return 0
        return 1
            
    def cargar_tablero(self,tablero):
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