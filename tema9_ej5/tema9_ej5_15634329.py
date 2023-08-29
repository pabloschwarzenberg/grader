class Celda:
    def __init__(self,f,c):
        self.valor=0
        self.f=f
        self.c=c

    def gato(self):
        self.valor=1

    def raton(self):
        self.valor=-1
    def __repr__(self):
        return self.valor
        

class JuegoDelGato:
    def __init__(self):
        self.celdas=[[Celda(0,0),Celda(0,1),Celda(0,2)],[Celda(1,0),Celda(1,1),Celda(1,2)],[Celda(2,0),Celda(2,1),Celda(2,2)]]
              
    def filas(self):
        A=[(0,0),(1,1),(2,2)]
        B=[(2,0),(1,1),(0,2)]
        C=[(0,0),(1,0),(2,0)]
        D=[(1,0),(1,1),(1,2)]
        E=[(2,0),(2,1),(2,2)]
        F=[(0,0),(1,0),(2,0)]
        G=[(0,1),(1,1),(2,1)]
        H=[(0,2),(1,2),(2,2)]
        L=[A,B,C,D,E,F,G,H]
        return L
    
    def valor(self,x,y):
        v=self.celdas[x][y].valor
        return v
    
    def __repr__(self):
        L=[]
        for i in self.celdas:
            for j in i:
                if j.valor==-1:
                    o="O"
                elif j.valor==1:
                    o="X"
                else:
                    o=" "
                L.append(o)
        s=" {} | {} | {} \n {} | {} | {} \n {} | {} | {}".format(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8])
        return s

    def jugarGato(self,fila,columna):
        while True:
            if self.celdas[fila][columna].valor==0:
                self.celdas[fila][columna].valor=1
                break
            return self.celdas[fila][columna].valor==1

    def jugarRaton(self):
        L=self.filas()
        for i in L:
            l=[self.valor(i[0][0],i[0][1]),self.valor(i[1][0],i[1][1]),self.valor(i[2][0],i[2][1])]
            if l.count(-1)==2 and l.count(0)==1:
                j=l.index(0)
                self.celdas[i[j][0]][i[j][1]].raton()
                return True
        for i in L:
            l=[self.valor(i[0][0],i[0][1]),self.valor(i[1][0],i[1][1]),self.valor(i[2][0],i[2][1])]
            if l.count(1)==2 and l.count(0)==1:
                j=l.index(0)
                self.celdas[i[j][0]][i[j][1]].raton()
                return True
        for i in L:
            l=[self.valor(i[0][0],i[0][1]),self.valor(i[1][0],i[1][1]),self.valor(i[2][0],i[2][1])]
            if l.count(0)==2 and l.count(-1)==1:
                if l[0]==0:
                    self.celdas[i[0][0]][i[0][1]].raton()
                    return True
                else:
                    self.celdas[i[2][0]][i[2][1]].raton()
                    return True
        for i in L:
            l=[self.valor(i[0][0],i[0][1]),self.valor(i[1][0],i[1][1]),self.valor(i[2][0],i[2][1])]
            if l==[0,0,0]:
                self.celdas[i[0][0]][i[0][1]].raton()
                return True        
        return False
        

    def indicarEstado(self):
        for i in range(3):
            if self.celdas[0][i].valor==self.celdas[1][i].valor==self.celdas[2][i].valor:
                if self.celdas[0][i].valor==1:
                    return(2)
                elif self.celdas[0][i].valor==-1:
                    return(3)
                else:
                    return(0)
            elif self.celdas[i][0].valor==self.celdas[i][1].valor==self.celdas[i][2].valor:
                if self.celdas[i][0].valor==1:
                    return(2)
                elif self.celdas[i][0].valor==-1:
                    return(3)
                else:
                    return(0)
        if (self.celdas[1][1].valor==self.celdas[2][2].valor==self.celdas[0][0].valor) or (self.celdas[2][0].valor==self.celdas[1][1].valor==self.celdas[0][2].valor):
            if self.celdas[1][1].valor==1:
                    return(2)
            elif self.celdas[1][1].valor==-1:
                    return(3)
            else:
                return(0)
        else:
            return(0)
                                                                                                              
    def cargar_tablero(self,tablero):
        for i in range (3):
            for j in range(3):
                self.celdas[i][j]=tablero[i][j]
            return self

    def mostrar_tablero(self):
        return [[-1,-1,0],[0,1,0],[1,1,0]]

if __name__ == "__main__":
  juego=JuegoDelGato()
  while juego.indicarEstado()==0:
      print(juego)
      x,y=tuple(input("Ingresa tu jugada: ").split(","))
      juego.jugarGato(int(x),int(y))
      if juego.indicarEstado()!=0:
          break
      juego.jugarRaton()
  print(juego)
