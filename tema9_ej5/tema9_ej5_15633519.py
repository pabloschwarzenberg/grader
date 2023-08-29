class JuegoDelGato:

    def __init__(self):
        self.tablero=[[1,0,0],[0,1,0],[0,0,1]]
        pass

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False

    def jugarRaton(self):
        
        pass

    def indicarEstado(self):

        for i in range(len(self.tablero)):
            if self.tablero[i][0]==self.tablero[i][1]==self.tablero[i][2] and self.tablero[i][0]!=0:
                if self.tablero[i][0]==1:
                    return 2
                else:
                    return 3
        for i in range(len(self.tablero)):
            if self.tablero[0][i]==self.tablero[1][i]==self.tablero[2][i] and self.tablero[0][i]!=0:
                if self.tablero[0][1]==1:
                    return 2
                else:
                    return 3

        if self.tablero[0][0]==self.tablero[1][1]==self.tablero[2][2] and self.tablero[1][1]!=0:
                if self.tablero[1][1]==1:
                    return 2
                else:
                    return 3

        if self.tablero[0][2]==self.tablero[1][1]==self.tablero[2][0] and self.tablero[1][1]!=0:
                if self.tablero[1][1]==1:
                    return 2
                else:
                    return 3
        i=0
        j=0

        while i<len(self.tablero):
            while j<len(self.tablero):
                if self.tablero[i][j]==0:
                    return 0
                j+=1
            i+=1
            j=0

            if i==len(self.tablero):
                return 1

    def cargar_tablero(self,tablero):
        self.tablero=tablero

    def mostrar_tablero(self):
        s=""
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                s+="{0: >5} ".format(self.tablero[i][j])
            s+="\n"
        return s

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         