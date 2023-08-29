class JuegoDelGato:
    def _init_(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Tablero vacío
        self.turno = 1 # Empieza el gato

    def jugarGato(self, fila, columna):
        # Verificar si la casilla está libre
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1 # Asignar casilla al gato
            self.turno = -1 # Cambiar turno
            return True
        else:
            return False

    def jugarRaton(self):
        # Verificar si hay casillas vacías
        casillas_vacias = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == 0]
        if len(casillas_vacias) == 0:
            return False # No se puede jugar

        # Verificar si el ratón puede ganar en el siguiente turno
        for fila, columna in casillas_vacias:
            self.tablero[fila][columna] = -1 # Asignar casilla al ratón
            if self.indicarEstado() == 3:
                self.turno = 1 # Cambiar turno
                return True
            self.tablero[fila][columna] = 0 # Deshacer jugada

        # Verificar si el gato puede ganar en el siguiente turno y bloquearlo
        for fila, columna in casillas_vacias:
            self.tablero[fila][columna] = 1 # Asignar casilla al gato
            if self.indicarEstado() == 2:
                self.tablero[fila][columna] = -1 # Deshacer jugada del gato
                self.turno = 1 # Cambiar turno
                return True
            self.tablero[fila][columna] = 0 # Deshacer jugada

        # Jugar en una casilla vacía al azar
        fila, columna = random.choice(casillas_vacias)
        self.tablero[fila][columna] = -1 # Asignar casilla al ratón
        self.turno = 1 # Cambiar turno
        return True

    def mostrar_tablero(self):
        return [[x if x != -1 else "R" for x in fila] for fila in self.tablero]

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar empate
        if all(x != 0 for fila in self.tablero for x in fila):
            return 1

        # Verificar ganador en filas
        for fila in self.tablero:
            if all(x == 1 for x in fila):
                return 2
            elif all(x == -1 for x in fila):
                return 3

        # Verificar ganador en columnas
        for j in range(3):
            if all(self.tablero[i][j] == 1 for i in range(3)):
                return 2
            elif all(self.tablero[i][j] == -1 for i in range(3)):
                return 3

        # Verificar ganador en diagonales
        if self.tablero[0][0] == 1 and self.tablero[1][1] == 1 and self.tablero[2][2] == 1:
            return 2
        elif self.tablero[0][2] == 1 and self.tablero[1][1] == 1 and self.tablero[2][0] == 1:
            return 2
        elif self.tablero[0][0] == -1 and self.tablero[1][1] == -1 and self.tablero[2][2] == -1:
            return 3
        elif self.tablero[0][2] == -1 and self.tablero[1][1] == -1 and self.tablero[2][0] == -1:
            return 3

        # No hay ganador pero se puede seguir jugando
        return 0
        