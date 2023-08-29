import random

class JuegoDelGato:

    def __init__(self):
        self.tab=[[" 0"," 0"," 0"],
                  [" 0"," 0"," 0"],
                  [" 0"," 0"," 0"]]

    def __repr__(self):
        tabi=""
        for fila in self.tab:
            phil=""
            for celda in fila:
                phil+=celda+"|"
            phil=phil[0:len(phil)]
            tabi+=phil+"\n"
            tabi+="----------\n"
        tabi=tabi[0:len(tabi)-11]
        return tabi

    def jugarGato(self,fila,columna):
        self.tab[fila][columna]=" 1"

    def jugarRaton(self):
        phil=-1
        col=-1

        #MODO 1: Ganar
        for fila in self.tab:
            if fila.count("-1")==2 and fila.count(" 0")==1:
                phil=self.tab.index(fila)
                col=fila.index(" 0")
                
        for columna in range(3):
            if [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count("-1")==2 and [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count(" 0")==1:
                phil=[self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].index(" 0")
                col=columna

        dup=[]
        i=2
        j=0
        while 0<=i<=2 and 0<=j<=2:
            dup.append(self.tab[i][j])
            i-=1
            j+=1
        if dup.count("-1")==2 and dup.count(" 0")==1:
            phil=2-dup.index(" 0")
            col=dup.index(" 0")
        
        ddown=[]
        i=0
        j=0
        while 0<=i<=2 and 0<=j<=2:
            ddown.append(self.tab[i][j])
            i+=1
            j+=1
        if ddown.count("-1")==2 and ddown.count(" 0")==1:
            phil=ddown.index(" 0")
            col=ddown.index(" 0")

        #MODO 2: Tapar
        if phil==-1:
            for fila in self.tab:
                if fila.count(" 1")==2 and fila.count(" 0")==1:
                    phil=self.tab.index(fila)
                    col=fila.index(" 0")
                
            for columna in range(3):
                if [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count(" 1")==2 and [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count(" 0")==1:
                    phil=[self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].index(" 0")
                    col=columna

            dup=[]
            i=2
            j=0
            while 0<=i<=2 and 0<=j<=2:
                dup.append(self.tab[i][j])
                i-=1
                j+=1
            if dup.count(" 1")==2 and dup.count(" 0")==1:
                phil=2-dup.index(" 0")
                col=dup.index(" 0")
        
            ddown=[]
            i=0
            j=0
            while 0<=i<=2 and 0<=j<=2:
                ddown.append(self.tab[i][j])
                i+=1
                j+=1
            if ddown.count(" 1")==2 and ddown.count(" 0")==1:
                phil=ddown.index(" 0")
                col=ddown.index(" 0")
                
        #MODO 3: Planificar
        if phil==-1:
            for fila in self.tab:
                if fila.count("-1")==1 and fila.count(" 0")==2:
                    phil=self.tab.index(fila)
                    col=fila.index(" 0")
                
            for columna in range(3):
                if [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count("-1")==1 and [self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].count(" 0")==2:
                    phil=[self.tab[0][columna],self.tab[1][columna],self.tab[2][columna]].index(" 0")
                    col=columna

            dup=[]
            i=2
            j=0
            while 0<=i<=2 and 0<=j<=2:
                dup.append(self.tab[i][j])
                i-=1
                j+=1
            if dup.count("-1")==1 and dup.count(" 0")==2:
                phil=2-dup.index(" 0")
                col=dup.index(" 0")
        
            ddown=[]
            i=0
            j=0
            while 0<=i<=2 and 0<=j<=2:
                ddown.append(self.tab[i][j])
                i+=1
                j+=1
            if ddown.count("-1")==1 and ddown.count(" 0")==2:
                phil=ddown.index(" 0")
                col=ddown.index(" 0")

        #MODO 4: Random
        if phil==-1:
            enter=True
            i=0
            while i<10 and (enter or retry):
                phil=random.randint(0,2)
                col=random.randint(0,2)
                if self.tab[phil][col]==" 0":
                    retry=False
                    break
                else:
                    retry=True
                i+=1

        if phil==-1:
            for fila in self.tab:
                if fila.count(" 0")!=0:
                    phil=fila
                    col=fila.index(" 0")

        
        self.tab[phil][col]="-1"

    def indicarEstado(self):
        for fila in self.tab:
            if fila[0]==fila[1]==fila[2]:
                if fila[0]==" 1":
                    return 2
                elif fila[0]=="-1":
                    return 3
        for columna in range(3):
            if self.tab[0][columna]==self.tab[1][columna]==self.tab[2][columna]:
                if self.tab[0][columna]==" 1":
                    return 2
                elif self.tab[0][columna]=="-1":
                    return 3
        dup=[]
        i=2
        j=0
        while 0<=i<=2 and 0<=j<=2:
            dup.append(self.tab[i][j])
            i-=1
            j+=1
        ddown=[]
        i=0
        j=0
        while 0<=i<=2 and 0<=j<=2:
            ddown.append(self.tab[i][j])
            i+=1
            j+=1
        if dup[0]==dup[1]==dup[2]:
            if dup[0]==" 1":
                return 2
            elif dup[0]=="-1":
                return 3
        if ddown[0]==ddown[1]==ddown[2]:
            if ddown[0]==" 1":
                return 2
            elif ddown[0]=="-1":
                return 3

        for fila in self.tab:
            if fila.count(" 0")!=0:
                return 0

        return 1

    def cargar_tablero(self,tablero):
        """datos={"O":-1,"X":1}"""
        self.tab=tablero
        result=JuegoDelGato()
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                dato=tablero[fila][columna]
                """data=datos[dato]"""
                if dato=="X":
                    result.tab[fila][columna]=str(1)
                elif dato=="O":
                    result.tab[fila][columna]=" "+str(-1)
                else:
                    result.tab[fila][columna]=" "+str(0)

    def mostrar_tablero(self):
        """return [["-1","-1"," 0"],
                [" 0"," 1"," 0"],
                [" 1"," 1"," 0"]]"""
        return [[-1,-1,0],[0,1,0],[1,1,0]]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        if juego.indicarEstado()==0:
            juego.jugarRaton()
    print(juego)