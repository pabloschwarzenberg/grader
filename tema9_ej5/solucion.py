class JuegoDelGato:

    def __init__(self):
        self.tablero = [ [0,0,0], [0,0,0], [0,0,0] ]
        self.estado_juego=0

    def __repr__(self):
        tab=""
        for i in range(0,3):
            lin=""
            for j in range(0,3):
                if self.tablero[i][j]==0:
                    tab=tab+" |"
                elif self.tablero[i][j]==-1:
                    tab=tab+"O|"
                elif self.tablero[i][j]==1:
                    tab=tab+"X|"
            tab+=lin+"\n"
        return tab

    def transponer(self):
        transpuesta=[]
        for i in range(0,3):
            fila=[]
            for j in range(0,3):
                fila.append(self.tablero[j][i])
            transpuesta.append(fila)
        return transpuesta

    def chequear(self):
        h1=sum(self.tablero[0])
        h2=sum(self.tablero[1])
        h3=sum(self.tablero[2])
        v1=self.tablero[0][0]+self.tablero[1][0]+self.tablero[2][0]
        v2=self.tablero[0][1]+self.tablero[1][1]+self.tablero[2][1]
        v3=self.tablero[0][2]+self.tablero[1][2]+self.tablero[2][2]
        d1=self.tablero[0][0]+self.tablero[1][1]+self.tablero[2][2]
        d2=self.tablero[0][2]+self.tablero[1][1]+self.tablero[2][0]
        r=[(0,h1),(1,h2),(2,h3),(3,v1),(4,v2),(5,v3),(6,d1),(7,d2)]
        return r

    def victoria(self,n):
        if n[1]==-3:
            return True
        else:
            return False

    def fracaso(self,n):
        if n[1]==3:
            return True
        else:
            return False

    def peligro(self,n):
        if n[1]==2:
            return True
        else:
            return False

    def posibilidad(self,n):
        if n[1]==-2:
            return True
        else:
            return False

    def avance(self,n):
        if n[1] in [-1,0]:
            return True
        else:
            return False

    def bloqueo(self,n):
        if n[1] == 1:
            return True
        else:
            return False

    def jugarHorizontal(self,fila):
        if 0 in self.tablero[fila]:
            i=self.tablero[fila].index(0)
            self.tablero[fila][i]=-1
            return True
        else:
            return False

    def jugarVertical(self,columna):
        self.tablero=self.transponer()
        r=self.jugarHorizontal(columna)
        self.tablero=self.transponer()
        return r

    def jugarDiagonal1(self):
        if self.tablero[0][0]==0:
            self.tablero[0][0]=-1
            return True
        elif self.tablero[1][1]==0:
            self.tablero[1][1]=-1
            return True
        elif self.tablero[2][2]==0:
            self.tablero[2][2]=-1
            return True
        return False

    def jugarDiagonal2(self):
        if self.tablero[0][2]==0:
            self.tablero[0][2]=-1
            return True
        elif self.tablero[1][1]==0:
            self.tablero[1][1]=-1
            return True
        elif self.tablero[2][0]==0:
            self.tablero[2][0]=-1
            return True
        return False

    def jugar(self,opciones):
        for opcion in opciones:
            if opcion[0] < 3:
                if self.jugarHorizontal(opcion[0]):
                    return True
            elif opcion[0] < 6:
                if self.jugarVertical(opcion[0]-3):
                    return True
            elif opcion[0] == 6:
                if self.jugarDiagonal1():
                    return True
            else:
                if self.jugarDiagonal2():
                    return True
        return False

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]!=0:
            return False
        else:
            self.tablero[fila][columna]=1
            return True

    def jugarRaton(self):
        estado=self.chequear()
        ganador=list(filter(self.victoria,estado))
        if len(ganador)!=0:
            self.estado_juego=3
            return False
        ganador=list(filter(self.fracaso,estado))
        if len(ganador)!=0:
            self.estado_juego=2
            return False
        posibilidades=list(filter(self.posibilidad,estado))
        if self.jugar(posibilidades):
            self.estado_juego=3
            return True

        ataques=list(filter(self.peligro,estado))
        if self.jugar(ataques):
            return True

        if self.tablero[1][1]==0:
            self.tablero[1][1]=-1
            return True

        avances=list(filter(self.avance,estado))
        if self.jugar(avances):
            return True

        bloqueos=list(filter(self.bloqueo,estado))
        if self.jugar(bloqueos):
            return True

        self.estado_juego=1
        return False

    def indicarEstado(self):
        return self.estado_juego

    def cargar_tablero(self,tablero):
        self.tablero=tablero

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