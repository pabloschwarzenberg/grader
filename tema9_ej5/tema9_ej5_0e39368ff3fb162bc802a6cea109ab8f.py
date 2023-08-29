import random
class JuegoDelGato:
    def __init__(self,longitud=3):
        self.longitud=longitud
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        tablero_str=""
        lineas=0
        for i in self.tablero:
            linea=""
            for j in i:
                linea+=str(j)
                if len(linea)<((self.longitud*2)-1):
                    linea+=","
                else:
                    linea+=""
            if lineas==0:
                tablero_str+=linea
            else:
                tablero_str+="\n"+linea
            lineas+=1
        return tablero_str

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False

    def jugarRaton(self):
        a=random.randint(0,2)
        b=random.randint(0,2)
        while self.tablero[a][b]!=0:
            a=random.randint(0,2)
            b=random.randint(0,2)
        if self.tablero[a][b]==0:
            self.tablero[a][b]=-1
            return True
        else:
            return False
        
    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self,matriz):
        self.tablero=matriz
        return self.tablero

    def indicarEstado(self):
        gato=0
        raton=0
        contador=0
        for i in self.tablero:
            for j in i:
                if j==1:
                    contador+=1
                    gato+=1
                elif j==-1:
                    contador+=1
                    raton+=1
                else:
                    gato=0
                    raton=0
            if gato==3:
                return 2
            elif raton==3:
                return 3
            elif contador==9:
                return 1
         return 0

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         