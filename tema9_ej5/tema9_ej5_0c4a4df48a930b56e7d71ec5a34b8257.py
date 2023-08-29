from random import randint



class JuegoDelGato:

    def __init__(self):
       self.fila1 = ["   ", "   ", "   "]
       self.fila2 = ["   ", "   ", "   "]
       self.fila3 = ["   ", "   ", "   "]
       self.tablero = [self.fila1, self.fila2, self.fila3]
       self.matriz = []
    

    def __repr__(self):
       
            print(" ") 

            print( " "+self.tablero[0][0]+" | "+self.tablero[0][1]+" | "+self.tablero[0][2] )
            print( " ----+-----+-----" )
            print( " "+self.tablero[1][0]+" | "+self.tablero[1][1]+" | "+self.tablero[1][2] )
            print( " ----+-----+-----" )
            print( " "+self.tablero[2][0]+" | "+self.tablero[2][1]+" | "+self.tablero[2][2] )
            for i in range(2):
                print( "") 
            return ""

    def jugarGato(self,fila,columna):
        i = int(fila)-1
        j = int(columna)-1
        if self.tablero[i][j]=="   ":
            self.tablero[i].pop(j)
            self.tablero[i].insert(j, " O ")
            return True
        else:
            return False
        

    def jugarRaton(self):
        while True:
            i = randint(1,3)-1
            j = randint(1,3)-1
            if self.tablero[i][j]=="   ":
                self.tablero[i].pop(j)
                self.tablero[i].insert(j, " X ")
                return True
                break
            else:
                return False
        
     

    def indicarEstado(self):
        a = str(self.tablero[0][0])+str(self.tablero[0][1])+str(self.tablero[0][2])
        b = str(self.tablero[1][0])+str(self.tablero[1][1])+str(self.tablero[1][2])
        c = str(self.tablero[2][0])+str(self.tablero[2][1])+str(self.tablero[2][2])
        d = str(self.tablero[0][0])+str(self.tablero[0][1])+str(self.tablero[0][2])
        e = str(self.tablero[0][1])+str(self.tablero[1][1])+str(self.tablero[2][1])
        f = str(self.tablero[0][2])+str(self.tablero[1][2])+str(self.tablero[2][2])
        g = str(self.tablero[0][0])+str(self.tablero[1][1])+str(self.tablero[2][2])
        h = str(self.tablero[0][2])+str(self.tablero[1][1])+str(self.tablero[2][0])
        if a==" X  X  X " or b==" X  X  X " or c==" X  X  X " or d==" X  X  X " or e==" X  X  X " or f==" X  X  X " or g==" X  X  X " or h==" X  X  X ":
            print(" Gato gana")
            return 2
        elif a==" O  O  O " or b==" O  O  O " or c==" O  O  O " or d==" O  O  O " or e==" O  O  O " or f==" O  O  O " or g==" O  O  O " or h==" O  O  O ":
            print(" Raton gana")
            return 3
        else:
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j]=="   ":
                        print(" Quedan jugadas")
                        return 0
            else:
                print(" Empate")
                return 1

    def cargar_tablero(self,matriz):
        matriz = self.tablero[:]
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j]=="   ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, 0)
                elif self.tablero[i][j]==" X ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, 1)
                elif self.tablero[i][j]==" O ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, -1)
        matriz = self.tablero
        return matriz
        

    def mostrar_tablero(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j]=="   ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, 0)
                elif self.tablero[i][j]==" X ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, 1)
                elif self.tablero[i][j]==" O ":
                    self.tablero[i].pop(j)
                    self.tablero[i].insert(j, -1)
        print(self)
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)