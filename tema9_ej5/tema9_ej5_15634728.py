class JuegoDelGato():    
    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        simbolos = {0:" ",1:"X",-1:"O"}
        t = [[simbolos[fila[i]] for i in range(3)] for fila in self.tablero]
        tablero = ""
        for fila in t:
            tablero += " " + " | ".join(fila)+"\n"
            tablero += "---+---+---\n"
        return tablero[:-13]

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        return False
        
    def jugarRaton(self):
        jugadas = []
        # Horizontal
        for i in range(3):
            if sum(self.tablero[i]) == 2:
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        jugadas.append((i,j))
        # Vertical
        for j in range(3):
            if sum(fila[j] for fila in self.tablero) == 2:
                for i in range(3):
                    if self.tablero[i][j] == 0:
                        jugadas.append((i,j))
        # Diagonal
        if sum(self.tablero[i][i] for i in range(3)) == 2:
            for i in range(3):
                if self.tablero[i][i] == 0:
                    jugadas.append((i,j))
        if sum(self.tablero[i][2-i] for i in range(3)) == 2:
            for i in range(3):
                if self.tablero[i][2-i] == 0:
                    jugadas.append((i,j))
        jugadas.sort()
        if jugadas != []:
            jugada = jugadas[0]
            self.tablero[jugada[0]][jugada[1]] = -1
            return True
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        return False

    def indicarEstado(self):
        ganadores = {3:2,-3:3}
        # Horizontal
        for fila in self.tablero:
            if sum(fila) == 3 or sum(fila) == -3:
                return ganadores[sum(fila)]
        # Vertical
        for i in range(3):
            if sum(fila[i] for fila in self.tablero) == 3 or sum(fila[i] for fila in self.tablero) == -3:
                return ganadores[sum(fila[i] for fila in self.tablero)]
        # Diagonal
        if sum(self.tablero[i][i] for i in range(3)) == 3 or sum(self.tablero[i][i] for i in range(3)) == -3:
            return ganadores[sum(self.tablero[i][i] for i in range(3))]
        if sum(self.tablero[i][2-i] for i in range(3)) == 3 or sum(self.tablero[i][2-i] for i in range(3)) == -3:
            return ganadores[sum(self.tablero[i][2-i] for i in range(3))]
        for fila in self.tablero:
            if 0 in fila:
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
