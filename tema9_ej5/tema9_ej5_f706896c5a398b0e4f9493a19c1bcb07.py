import random
class JuegoDelGato:

    def __init__(self):
        self.tablero=[]


    def repr(self):
        for row in self.tablero:
            print(row)

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False

    def jugarRaton(self):
        if not(self.rat_win()):
            while True:
                fila=random.randint(0,2)
                columna=random.randint(0,2)
                if self.tablero[fila][columna]==0:
                    self.tablero[fila][columna]=-1
                    break
        return True
                
    def rat_win(self):
        count=1
        check=-2
        while count<=2:
            bred=self.bredd()
            for i in range(len(bred)):
                if bred[i]==check:
                    for pos in range(len(self.tablero[i])):
                        if self.tablero[i][pos]==0:
                            self.tablero[i][pos]=-1
                            return True
            langd=self.langd()
            for i in range(len(langd)):
                if langd[i]==check:
                    for row in range(len(self.tablero[i])):
                        if self.tablero[row][i]==0:
                            self.tablero[row][i]=-1
                            return True
            diag=self.diagonal()
            if diag[0]==check:
                i=0
                for row in range(len(self.tablero[i])):
                        if self.tablero[row][i]==0:
                            self.tablero[row][i]=-1
                            return True
                        i+=1
            elif diag[1]==check:
                i=2
                for row in range(len(self.tablero[i])):
                        if self.tablero[row][i]==0:
                            self.tablero[row][i]=-1
                            return True
                        i-=1
            check=2
            count+=1
        return False

    def bredd(self):
        positioner=[]
        for row in self.tablero:
            t=0
            for ruta in row:
                t+=ruta
            positioner.append(t)
        return positioner

    def langd(self):
        positioner=[]
        for i in range(len(self.tablero[0])):
            kol=0
            for row in self.tablero:
                kol+=row[i]
            positioner.append(kol)
        return positioner

    def diagonal(self):
        positioner=[]
        dia1=0
        i=0
        for row in self.tablero:
            dia1+=row[i]
            i+=1
        positioner.append(dia1)    
        dia2=0
        i=2
        for row in self.tablero:
            dia2+=row[i]
            i-=1
        positioner.append(dia2)
        return positioner
        
    def ganador(self):
        estado=self.indicarEstado()
        if estado==1:
            print("Empate")
            return True
        elif estado==2:
            print("Ganó el gato!")
            return True
        elif estado==3:
            print("Ganó el raton!")
            return True
        else:
            return False
        
    def indicarEstado(self):
        for row in self.tablero:
            t=0
            for ruta in row:
                t+=ruta
            if t==3:
                return 2
            elif t==-3:
                return 3
     
        for i in range(len(self.tablero[0])):
            kol=0
            for row in self.tablero:
                kol+=row[i]
            if kol==3:
                return 2
            elif kol==-3:
                return 3
        dia1=0
        i=0
        for row in self.tablero:
            dia1+=row[i]
            i+=1
        dia2=0
        i=2
        for row in self.tablero:
            dia2+=row[i]
            i-=1
        if dia1==3 or dia2==3:
            return 2
        elif dia1==-3 or dia2==-3:
            return 3
        for row in self.tablero:
            if 0 in row:
                return 0
        return 1
           
    def cargar_tablero(self,tablero):
        self.tablero=tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    tablero=[[0,0,0],[0,0,0],[0,0,0]]
    juego.cargar_tablero(tablero)
    while juego.indicarEstado()==0:
        juego.repr()
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        if juego.ganador():
            break
        juego.jugarRaton()
        if juego.ganador():
            break
    juego.repr()

         