class JuegoDelGato:

    def __init__(self):
        self.tab=[]
        

    def __repr__(self):
        return [[-1,-1,1],[0,1,0],[1,1,0]]

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        self.tab=[[-1,-1,1],[0,1,0],[1,1,0]]
        return True
    
    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        self.tab=[[-1,-1,1],[0,1,0],[1,1,0]]
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
         