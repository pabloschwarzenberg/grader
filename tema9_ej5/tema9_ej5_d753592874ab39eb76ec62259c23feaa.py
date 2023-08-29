import random

class JuegoDelGato:

    def __init__(self):
       a=[random.randint(0,3), random.randint(0,3)]
       b=[random.randint(0,3), random.randint(0,3)]
       c=[random.randint(0,3), random.randint(0,3)]
       self.filas=[]
       self.columnas=[]
       
       for i in range(3):  ### Filas
            for j in range(3):  #### Columnas
                self.columnas.append(" ")
            self.filas.append(columnas)
            
       for i in range(3):  ### Filas
            for j in range(3):  #### Columnas
                if i==a[0] and j==a[1]:
                    
                self.columnas.append(" ")
            self.filas.append(columnas)
        
    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        pass

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
         