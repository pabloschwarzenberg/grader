class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementa aquí la lógica para que el ratón juegue de forma inteligente
        # según la configuración del tablero
        # Puedes usar cualquier algoritmo o estrategia que consideres adecuada
        return True

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz

    def indicarEstado(self):
        # Implementa aquí la lógica para determinar el estado del juego:
        # 0 si no hay ganador pero se puede seguir jugando
        # 1 si hay empate
        # 2 si ganó el gato
        # 3 si ganó el ratón
        return 0


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)

         