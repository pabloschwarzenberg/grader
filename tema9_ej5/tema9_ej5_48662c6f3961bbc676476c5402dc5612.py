class JuegoDelGato:

    def __init__(self):
        self.matriz = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.matriz[columna][fila] == 0:
            self.matriz[columna][fila] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] == 0:
                    self.matriz[i][j] = -1
                    return True
        
        return False

    def indicarEstado(self):
        condiciones = [
            (self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2]),
            (self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2]),
            (self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2]),
            (self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0]),
            (self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1]),
            (self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2]),
            (self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2]),
            (self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0])
        ]
        if condiciones[0] == True or condiciones[1] == True or condiciones[2] == True or condiciones[3] == True or condiciones[4] == True or condiciones[5] == True or condiciones[6] == True or condiciones[7] == True:
            if condiciones[7] == True or condiciones[6] == True or condiciones[4] == True or condiciones[1] == True:
                if self.matriz[1][1] == 1:
                    return 2
                if self.matriz[1][1] == -1:
                    return 3
            
            elif condiciones[0] == True or condiciones[3] == True:
                if self.matriz[0][0] == 1:
                    return 2
                if self.matriz[0][0] == -1:
                    return 3
            
            elif condiciones [2] == True or condiciones[5] == True:
                if self.matriz[2][2] == 1:
                    return 2
                if self.matriz[2][2] == -1:
                    return 3
                
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] == 0:
                    return 0
                
        return 1

    def cargar_tablero(self,tablero):
        self.matriz = tablero

    def mostrar_tablero(self):
        return self.matriz

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         