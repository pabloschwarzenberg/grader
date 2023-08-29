class JuegoDelGato:

    def __init__(self):
        self.1=[0,0,0]
        self.2=[0,0,0]
        self.3=[0,0,0]
        self.tablero=[self.1,self.2,self.3]
    
    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
       
        self.fila=fila
        pudo=False
        if self.fila==1:
            elif self.1[0]==self.2[0]==self.3[0]== 1 or -1:
              pudo=True
        elif self.fila==2:
            elif self.1[1]==self.2[1]==self.3[1]== 1 or -1:
              pudo=True
        elif self.fila==3:
            elif self.1[2]==self.2[2]==self.3[2]== 1 or -1:
               pudo= True
        elif self.columna==1:
            elif self.1[0]==self.1[1]==self.1[2]== 1 or -1:
               pudo= True
        elif self.columna==2:
            elif self.2[0]==self.2[1]==self.2[2]== 1 or -1:
               pudo= True
        elif self.columna==3:
            elif self.3[0]==self.3[1]==self.3[2]== 1 or -1:
               pudo= True
        return pudo
        

    def jugarRaton(self):-1
    
        

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
    
        pass

    def mostrar_tablero(self):
        return [[-1,-1,0],[0,1,0],[1,1,0]]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         