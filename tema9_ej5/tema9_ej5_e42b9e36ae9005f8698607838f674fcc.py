class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def jugarGato(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        self.tablero[y][x] = 1

    def jugarRaton(self):
        decision_x = 69
        decision_y = 69
        if self.indicarEstado() != 0:
            return False
        else:
            y = 0
            while y < len(self.tablero):
                fila = self.tablero[y]
                x = 0
                while x < len(fila):
                    if fila[x] == 0:
                        marcas_gato = self.contar(x, y, 1, 69, [(x, y)], [])
                        if len(marcas_gato) > 2:
                            decision_x = x
                            decision_y = y
                            break
                        marcas_gato = self.contar(x, y, 0, 69, [(x, y)], [])
                        if len(marcas_gato) > 2:
                            decision_x = x
                            decision_y = y
                            break
                    x += 1
                y += 1
            if decision_x == 69:
                otras_opciones = [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)]
                for punto in otras_opciones:
                    x = punto[0]
                    y = punto[1]
                    if self.tablero[y][x] == 0:
                        decision_x = x
                        decision_y = y
                        break
            if decision_x == 69:
                y = 0
                while y < len(self.tablero):
                    fila = self.tablero[y]
                    x = 0
                    while x < len(fila):
                        if fila[x] == 0:
                            decision_x = x
                            decision_y = y
                            break
                        x += 1
                    y += 1
            print(str(decision_y) + ', ' + str(decision_x))
            self.tablero[decision_y][decision_x] = -1

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def contar(self, x, y, numero, pendiente, consecutivos, mayor):
        posiciones = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                      (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)]
        if pendiente != 69:
            posiciones = [posiciones[pendiente]]
        movimiento = 0
        while movimiento < len(posiciones):
            posicion = posiciones[movimiento]
            nueva_x = posicion[0]
            nueva_y = posicion[1]
            if 0 <= nueva_x < 3 and 0 <= nueva_y < 3:
                punto = nueva_x, nueva_y
                if self.tablero[nueva_y][nueva_x] == numero and punto not in consecutivos:
                    consecutivos = self.contar(nueva_x, nueva_y, numero, movimiento, consecutivos + [punto], mayor)
                    if len(consecutivos) > len(mayor):
                        mayor = consecutivos
            movimiento += 1
        return mayor

    def indicarEstado(self):
        espacios_libres = False
        y = 0
        while y < len(self.tablero):
            fila = self.tablero[y]
            x = 0
            while x < len(fila):
                if fila[x] != 0:
                    puntos = len(self.contar(x, y, fila[x], 69, [(x, y)], []))
                    if puntos >= 3 and fila[x] == 1:
                        return 2
                    if puntos >= 3 and fila[x] == -1:
                        return 3
                elif not espacios_libres:
                    espacios_libres = True
                x += 1
            y += 1
        if espacios_libres:
            return 0
        else:
            return 1

if __name__ == '__main__':
    juego = JuegoDelGato()
    while True:
        print('Este es el tablero:')
        tablero = juego.tablero
        for filaa in tablero:
            print(str(filaa))
        comando = input('¿Dónde vas a marcar? Escribe la posición en formato x,y: ')
        datos = comando.split(',')
        abscisa = int(datos[0])
        ordenada = int(datos[1])
        print(juego.indicarEstado())
        juego.jugarGato(abscisa, ordenada)
        juego.jugarRaton()
