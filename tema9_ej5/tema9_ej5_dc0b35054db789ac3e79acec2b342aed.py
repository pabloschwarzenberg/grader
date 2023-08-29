class JuegoDelGato:

    def __init__(self):
        # Inicializar el tablero con ceros
        self.tablero = [[0 for _ in range(3)] for _ in range(3)]

    def __repr__(self):
        # Mostrar el tablero con símbolos y separadores
        simbolos = {0: ".", 1: "X", -1: "O"}
        resultado = ""
        for i in range(3):
            for j in range(3):
                resultado += simbolos[self.tablero[i][j]]
                if j < 2:
                    resultado += "|"
            if i < 2:
                resultado += "\n" + "-" * 5 + "\n"
        return resultado

    def jugarGato(self,fila,columna):
        # Verificar si la jugada es válida
        if 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == 0:
            # Asignar el valor 1 al gato
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Priorizar las celdas centrales
        if self.tablero[1][1] == 0:
            self.tablero[1][1] = -1
            return True
        # Priorizar las esquinas
        for i in [0,2]:
            for j in [0,2]:
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        # Priorizar los bordes
        for i in [0,1,2]:
            for j in [0,1,2]:
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        # No hay celdas disponibles
        return False

    def indicarEstado(self):
        # Verificar si hay tres valores iguales en una fila, una columna o una diagonal
        def ganador(valor):
            # Filas
            for i in range(3):
                if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == valor:
                    return True
            # Columnas
            for j in range(3):
                if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] == valor:
                    return True
            # Diagonales
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == valor:
                return True
            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == valor:
                return True
            # No hay tres valores iguales
            return False

        # Retornar 2 si ganó el gato
        if ganador(1):
            return 2
        # Retornar 3 si ganó el ratón
        if ganador(-1):
            return 3
        # Verificar si hay alguna celda vacía
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    # Retornar 0 si se puede seguir jugando
                    return 0
        # Retornar 1 si hay empate
        return 1

    def cargar_tablero(self,matriz):
        # Reemplazar el tablero con la matriz recibida
        self.tablero = matriz

    def mostrar_tablero(self):
        # Retornar una copia del tablero
        return [fila[:] for fila in self.tablero]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
    estado = juego.indicarEstado()
    if estado == 1:
        print("Empate")
    elif estado == 2:
        print("Ganaste")
    elif estado == 3:
        print("Perdiste")
         