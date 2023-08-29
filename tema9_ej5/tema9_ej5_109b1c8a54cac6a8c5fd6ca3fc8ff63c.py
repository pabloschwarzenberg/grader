import time
class JuegoDelGato:

    def __init__(self):
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        return str(self.tablero)

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False

    def jugarRaton(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.tablero[i][j]==0:
                    self.tablero[i][j]=-1
                    if JuegoDelGato.indicarEstado(self)==3:
                        return True
                    else:
                        self.tablero[i][j]=0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.tablero[i][j]==0:
                    self.tablero[i][j]=1
                    if JuegoDelGato.indicarEstado(self)==2:
                        self.tablero[i][j]=-1
                        print("2")
                        return True
                    else:
                        self.tablero[i][j]=0

        if self.tablero[0][0]==0:
            self.tablero[0][0]=-1
            return True
        if self.tablero[2][0] == 0:
            self.tablero[2][0] = -1
            return True
        if self.tablero[0][2]==0:
            self.tablero[0][2]=-1
            return True
        if self.tablero[2][2]==0:
            self.tablero[2][2]=-1
            return True

        for i in range(0,3):
            for j in range(0,3):
                if self.tablero[i][j]==0:
                    self.tablero[i][j]=-1
                    return True
        else:
            return False

    def indicarEstado(self):
        for i in range(0,3):
            contador=0
            for j in range(0,3):
                if self.tablero[i][j]==1:
                    contador+=1
                    if contador==3:
                        return 2
        for i in range(0,3):
            contador=0
            for j in range(0,3):
                if self.tablero[j][i]==1:
                    contador+=1
                    if contador==3:
                        return 2
        contador=0
        for i in range(0,3):
            if self.tablero[i][i]==1:
                contador+=1
                if contador==3:
                    return 2
        if self.tablero[2][0]==1 and self.tablero[1][1]==1 and self.tablero[0][2]==1:
            return 2

        for i in range(0, 3):
            contador = 0
            for j in range(0, 3):
                if self.tablero[i][j] == -1:
                    contador += 1
                    if contador == 3:
                        return 3
        for i in range(0, 3):
            contador = 0
            for j in range(0, 3):
                if self.tablero[j][i] == -1:
                    contador += 1
                    if contador == 3:
                        return 3
        contador = 0
        for i in range(0, 3):
            if self.tablero[i][i] == -1:
                contador += 1
                if contador == 3:
                    return 3
        if self.tablero[2][0] == -1 and self.tablero[1][1] == -1 and self.tablero[0][2] == -1:
            return 3
        contador=0
        for i in range(0,3):
            for j in range(0,3):
                if self.tablero[i][j]==0:
                    contador+=1
        if contador==0:
            return 1

        return 0

    def mostrar_tablero(self):
        for i in range (0,3):
            for j in range (0,3):
                if self.tablero[i][j]==0:
                    self.tablero[i][j]=" "
                elif self.tablero[i][j]==1:
                    self.tablero[i][j]="X"
                elif self.tablero[i][j]==-1:
                    self.tablero[i][j]="O"
        return self.tablero

    def cargar_tablero(self,tablero):
        for i in range (0,3):
            for j in range (0,3):
                if tablero[i][j]==" ":
                    self.tablero[i][j]=0
                elif tablero[i][j]=="O":
                    self.tablero[i][j]=1
                elif tablero[i][j]=="X":
                    self.tablero[i][j]=-1

if __name__ == "__main__":
    juego=JuegoDelGato()
    juego.cargar_tablero([["O"," "," "],[" ","X"," "],["X","X"," "]])
    print(juego)
    while juego.indicarEstado()==0:
        print("Le toca al gato")
        y,x=tuple(input("Ingresa tu jugada: ").split(","))
        while juego.jugarGato(int(x),int(y))==False:
            y, x = tuple(input("Jugada incorrecta. Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        print(juego)
        if juego.indicarEstado()==0:
            print("El raton esta pensando..."+"\n")
            time.sleep(2)
            juego.jugarRaton()
            print(juego)
    if juego.indicarEstado()==1:
        print("Hubo un empate!")
    elif juego.indicarEstado()==2:
        print("Gano el gato!")
    elif juego.indicarEstado()==3:
        print("Gano el raton!")
