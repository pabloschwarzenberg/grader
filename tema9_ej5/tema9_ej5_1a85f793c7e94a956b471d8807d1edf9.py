class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1
        self.turno_gato = True

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            if self.turno_gato:
                self.tablero[fila][columna] = self.gato
                self.turno_gato = False
                return True
            else:
                return False
        else:
            return False

    def jugarRaton(self):
        mejores_jugadas = []
        mejor_puntaje = float('-inf')

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    puntaje = self.minimax(self.tablero, 0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejores_jugadas = [(fila, columna)]
                        mejor_puntaje = puntaje
                    elif puntaje == mejor_puntaje:
                        mejores_jugadas.append((fila, columna))

        if len(mejores_jugadas) > 0:
            fila, columna = mejores_jugadas[0]
            self.tablero[fila][columna] = self.raton
            self.turno_gato = True
            return True
        else:
            return False

    def minimax(self, estado, profundidad, es_maximizando):
        estado_actual = self.indicarEstado()
        if estado_actual != 0:
            return self.calcularPuntaje(estado_actual, profundidad)

        if es_maximizando:
            mejor_puntaje = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if estado[fila][columna] == 0:
                        estado[fila][columna] = self.raton
                        puntaje = self.minimax(estado, profundidad + 1, False)
                        estado[fila][columna] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            peor_puntaje = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if estado[fila][columna] == 0:
                        estado[fila][columna] = self.gato
                        puntaje = self.minimax(estado, profundidad + 1, True)
                        estado[fila][columna] = 0
                        peor_puntaje = min(peor_puntaje, puntaje)
            return peor_puntaje

    def calcularPuntaje(self, estado_actual, profundidad):
        if estado_actual == 1:
            return 0
        elif estado_actual == 2:
            return 10 - profundidad
        elif estado_actual == 3:
            return profundidad - 10

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero


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
         