import random
class JuegoDelGato:

    def __init__(self):
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        return "{}\n{}\n{}".format(self.tablero[0],self.tablero[1],self.tablero[2])

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False

    def jugarRaton(self):
        tablero=self.tablero
        while True:
            x=random.randint(0,2)
            y=random.randint(0,2)
            if tablero[x][y]==0:
                tablero[x][y]=-1
                p=0
                for i in range(3):
                    if tablero[i][i]==-1:
                        p+=1
                    k=s=0
                    for j in range(3):
                        if tablero[i][j]==-1:
                            k+=1
                        elif tablero[j][i]==-1:
                            s+=1
                if p==3 or k==3 or s==3:
                    self.tablero[x][y]=-1
                    break
                elif p==2 or k==2 or s==2:
                    self.tablero[x][y]=-1
                    break
                elif p==1 or k==1 or s==1:
                    self.tablero[x][y]=-1
                    break
                elif p==0 or k==0 or s==0:
                    self.tablero[x][y]=-1
                    break

    def indicarEstado(self):
        q=0
        p=0
        for i in range(3):
            if self.tablero[i][i]==1:
                q+=1
            elif self.tablero[i][i]==-1:
                p+=1
            n=0
            k=0
            r=0
            s=0
            for j in range(3):
                if self.tablero[i][j]==1:
                    n+=1
                elif self.tablero[i][j]==-1:
                    k+=1
                if self.tablero[j][i]==1:
                    r+=1
                elif self.tablero[j][i]==-1:
                    s+=1
            if n==3 or q==3 or r==3:
                return 2
            elif k==3 or p==3 or s==3:
                return 3
            else:
                for x in range(3):
                    if self.tablero[x].count(0)!=0:
                        return 0            

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
         
