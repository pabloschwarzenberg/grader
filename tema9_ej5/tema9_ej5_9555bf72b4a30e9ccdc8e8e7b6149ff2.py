class JuegoDelGato:
    def __init__(self):
        self.filas=[[0,0,0] for i in range(3)]
        self.columnas=[[0,0,0] for i in range(3)]
        self.diagonales=[[0,0,0],[0,0,0]]

    def __repr__(self):
        s=""
        for fila in self.filas:
            for x in fila:
                s+=str(x)
            s+="\n"
        return s

    def jugarGato(self,x,y,n=1):
        if self.filas[y][x]!=0:
            return False
        self.filas[y][x]=n
        self.columnas[x][y]=n
        if x==y:
            self.diagonales[0][x]=n
        if x==2-y:
            self.diagonales[1][y]=n
        return True

    def jugarRaton(self):
        jugadas=self.filas+self.columnas+self.diagonales
        valores=[]
        for i in range(len(jugadas)):
            if 0 in jugadas[i]:
                valores.append((sum(jugadas[i]),i))
        valores.sort()
        if len(valores)==0:
            return False
        if abs(valores[0][0])>=valores[-1][0]:
            indice=valores[0][1]
        else:
            indice=valores[-1][1]
        x=jugadas[indice].index(0)
        if 0<=indice<3:
            self.jugarGato(x,indice,-1)
        elif 3<=indice<6:
            self.jugarGato(indice-3,x,-1)
        elif indice==6:
            self.jugarGato(x,x,-1)
        else:
            self.jugarGato(2-x,x,-1)
            
    def indicarEstado(self):
        jugadas=self.filas+self.columnas+self.diagonales
        for x in jugadas:
            if 0 in x:
                return 0
        for x in jugadas:
            if [1,1,1]==x:
                return 2
            elif [-1,-1,-1]==x:
                return 3
        return 1

    def cargar_tablero(self,casillas):
        self.filas=casillas
        self.columnas=[[a[i] for a in casillas] for i in range(3)]
        self.diagonales=[[casillas[i][i] for i in range(3)],[casillas[i][2-i] for i in range(3)]]

    def mostrar_tablero(self):
        return self.filas

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         