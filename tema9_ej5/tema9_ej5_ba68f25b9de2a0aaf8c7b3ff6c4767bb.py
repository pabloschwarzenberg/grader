import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0 for i in range(3)] for j in range(3)]
        self.turno = 1

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        posibles_jugadas = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posibles_jugadas.append((i,j))
        if len(posibles_jugadas) == 0:
            return False
        else:
            jugada = random.choice(posibles_jugadas)
            self.tablero[jugada[0]][jugada[1]] = -1
            return True

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self,matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Revisa si hay un ganador en las filas
        for i in range(3):
            if sum(self.tablero[i]) == 3:
                return 2
            elif sum(self.tablero[i]) == -3:
                return 3
        
        # Revisa si hay un ganador en las columnas
        for j in range(3):
            suma_columna = 0
            for i in range(3):
                suma_columna += self.tablero[i][j]
            if suma_columna == 3:
                return 2
            elif suma_columna == -3:
                return 3
        
        # Revisa si hay un ganador en las diagonales
        diagonal_principal = [self.tablero[i][i] for i in range(3)]
        diagonal_secundaria = [self.tablero[i][2-i] for i in range(3)]
        
        if sum(diagonal_principal) == 3 or sum(diagonal_secundaria) == 3:
            return 2
        elif sum(diagonal_principal) == -3 or sum(diagonal_secundaria) == -3:
            return 3
        
        # Si no hay ganador y quedan casillas vacías, sigue el juego
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return 0
        
        # Si no hay ganador y no quedan casillas vacías, es empate
        return 1

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego.mostrar_tablero())
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        while not juego.jugarGato(int(x),int(y)):
            print("Jugada inválida")
            x,y=tuple(input("Ingresa tu jugada: ").split(","))
        
        juego.jugarRaton()
    print(juego.mostrar_tablero())
