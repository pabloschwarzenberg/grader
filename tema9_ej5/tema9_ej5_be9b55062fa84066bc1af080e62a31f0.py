import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]
        #el tablero como tal
    def __repr__(self):
        return "{}\n{}\n{}".format(self.tablero[0],self.tablero[1],self.tablero[2])
        #la representacion del tablero
    
    def jugarGato(self,fila,columna):
        self.tablero[fila][columna] = 1
        #esta sera la ficha jugada por un jugador
    def mostrar_tablero(self):
        return [self.tablero[0],self.tablero[1],self.tablero[2]]
        
    def definir_variables(self):
        h1= self.tablero[0]
        h2= self.tablero[1]
        h3= self.tablero[2]
        v1 = [self.tablero[0][0],self.tablero[1][0],self.tablero[2][0]]
        v2 = [self.tablero[0][1],self.tablero[1][1],self.tablero[2][1]]
        v3 = [self.tablero[0][2],self.tablero[1][2],self.tablero[2][2]]
        d1 = [self.tablero[0][0],self.tablero[1][1],self.tablero[2][2]]
        d2 = [self.tablero[0][2],self.tablero[1][1],self.tablero[2][0]]
        horizontales = [h1,h2,h3]
        verticales = [v1,v2,v3]
        diagonales = [d1,d2]
        ceros = 0
        unos = 0
        munos = 0
        conta = 0
        
    def revisa_horizontales(self):
        h1= self.tablero[0]
        h2= self.tablero[1]
        h3= self.tablero[2]
        v1 = [self.tablero[0][0],self.tablero[1][0],self.tablero[2][0]]
        v2 = [self.tablero[0][1],self.tablero[1][1],self.tablero[2][1]]
        v3 = [self.tablero[0][2],self.tablero[1][2],self.tablero[2][2]]
        d1 = [self.tablero[0][0],self.tablero[1][1],self.tablero[2][2]]
        d2 = [self.tablero[0][2],self.tablero[1][1],self.tablero[2][0]]
        horizontales = [h1,h2,h3]
        verticales = [v1,v2,v3]
        diagonales = [d1,d2]
        ceros = 0
        unos = 0
        munos = 0
        conta = 0
        for i in horizontales:
            for j in i:
                if j == 0:
                    ceros += 1
                if j == 1:
                    unos += 1
                if j == -1:
                    munos +=1
            if ceros == 1:
                if unos == 2:
                    winers.append('h'+str(conta))
                    listag.append(i)
                elif munos == 2:
                    losers.append('h'+str(conta))
                    listap.append(i)
            if unos == 3:
                ganador = 2
            if munos == 3:
                ganador = 3
            conta +=1
            ceros = 0
            unos = 0
            munos = 0
        #entrega las horizontales con [1,1,0] o [-1,-1,0]

    def revisa_verticales(self):
        h1= self.tablero[0]
        h2= self.tablero[1]
        h3= self.tablero[2]
        v1 = [self.tablero[0][0],self.tablero[1][0],self.tablero[2][0]]
        v2 = [self.tablero[0][1],self.tablero[1][1],self.tablero[2][1]]
        v3 = [self.tablero[0][2],self.tablero[1][2],self.tablero[2][2]]
        d1 = [self.tablero[0][0],self.tablero[1][1],self.tablero[2][2]]
        d2 = [self.tablero[0][2],self.tablero[1][1],self.tablero[2][0]]
        horizontales = [h1,h2,h3]
        verticales = [v1,v2,v3]
        diagonales = [d1,d2]
        ceros = 0
        unos = 0
        munos = 0
        conta = 0
        for i in verticales:
            for j in i:
                if j == 0:
                    ceros += 1
                if j == 1:
                    unos += 1
                if j == -1:
                    munos +=1
            if ceros == 1:
                if unos == 2:
                    winers.append('v'+str(conta))
                    listag.append(i)
                elif munos == 2:
                    losers.append('v'+str(conta))
                    listap.append(i)
            if unos == 3:
                ganador = 2
            if munos == 3:
                ganador = 3
            conta += 1
            ceros = 0
            unos = 0
            munos = 0


    def revisa_diagonales(self):
        h1= self.tablero[0]
        h2= self.tablero[1]
        h3= self.tablero[2]
        v1 = [self.tablero[0][0],self.tablero[1][0],self.tablero[2][0]]
        v2 = [self.tablero[0][1],self.tablero[1][1],self.tablero[2][1]]
        v3 = [self.tablero[0][2],self.tablero[1][2],self.tablero[2][2]]
        d1 = [self.tablero[0][0],self.tablero[1][1],self.tablero[2][2]]
        d2 = [self.tablero[0][2],self.tablero[1][1],self.tablero[2][0]]
        horizontales = [h1,h2,h3]
        verticales = [v1,v2,v3]
        diagonales = [d1,d2]
        ceros = 0
        unos = 0
        munos = 0
        conta = 0
        for i in diagonales:
            for j in i:
                if j == 0:
                    ceros += 1
                if j == 1:
                    unos += 1
                if j == -1:
                    munos += 1
            if ceros == 1:
                if unos == 2:
                    winers.append('d'+str(conta+1))
                    listag.append(i)
                elif munos == 2:
                    losers.append('d'+str(conta+1))
                    listap.append(i)
            if unos == 3:
                ganador = 2
            if munos == 3:
                ganador = 3
                conta +=1
            ceros = 0
            unos = 0
            munos = 0

    def jugarRaton(self):
        for i in listag:
            for j in i:
                listagstr.append(str(j))
        for i in listap:
            for j in i:
                listapstr.append(str(j))
        
        if len(winers) != 0:
            dato = winers.pop(0)
            if dato[0] == 'h':
                f = int(dato[1])
                c = int(listagstr.index("0"))
                
            if dato[0] == 'v':
                f = int(listagstr.index("0"))
                c = int(dato[1])
            
            if dato[0] == 'd':
                if dato[1] == '0':
                    f = int(listagstr.index("0"))
                    c = int(listagstr.index("0"))
                    
                if dato[1] == '1':
                    f = int(listagstr.index("0"))
                    c = int(2 - listagstr.index("0"))
                    
            self.tablero[f][c] = -1

        elif len(losers) != 0:
            dato = losers.pop(0)
            if dato[0] == 'h':
                f = dato[1]
                c = int(listapstr.index("0"))
                
            if dato[0] == 'v':
                f = int(listapstr.index("0"))
                c = dato[1]
                
            if dato[0] == 'd':
                if dato[1] == '1':
                    f = int(listapstr.index("0"))
                    c = int(listapstr.index("0"))
                    
                if dato[1] == '2':
                    f = int(listapstr.index("0"))
                    c = 2 - int(listapstr.index("0"))

            self.tablero[f][c] = -1
            
        else:
            i=0
            while i == 0:
                f = random.randint(0,2)
                c = random.randint(0,2)
                if self.tablero[f][c] == 0:
                    self.tablero[f][c] = -1
                    i=1
                    
        #ficha de la computadora
        
                    
    def cargar_tablero(self,matriz):
        self.tablero = matriz
        #reemplaza el tablero con una matriz de 3x3 recibida con valores 0,-1,1

    def indicarEstado(self):
        #el estado por defecto en el programa será 1 de empate.
        #al revisar todo, se dara oportunidad al juego de modificar tal estado
        #la funcion indicarestado va a verificar que se pueda seguir jugando si no hay ganador
        if ganador == 2:
            return 2
        elif ganador == 3:
            return 3
        for i in self.tablero:
            for j in i:
                if j == 0:
                    return 0
        else:
            return 1
        #0 si no hay ganador pero se puede seguir jugando
        #1 si hay empate
        #2 si gano el gato
        #3 si gano el raton
   
ganador = 0
winers = []
losers = []
listag = []
listap = []
listagstr = []
listapstr = []

if __name__ == "__main__":
    juego=JuegoDelGato()
    juego.definir_variables()
    ganador = 0
    tablero = repr(juego)
    print(tablero)
    while juego.indicarEstado()==0:
        juego.definir_variables()
        ###
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        ###
        tablero = repr(juego)
        print(tablero)
        ###
        final = juego.indicarEstado()
        if final == 1:
            print("Se ha finalizado en un empate")
            n = input()
            break
        if final == 2:
            print("ganaste")
            n = input()
            break
        if final == 3:
            print("perdiste")            
            n = input()
            break
        ###
        z = input("Estás listo para ver la jugada de la maquina?")
        ###
        juego.revisa_horizontales()
        juego.revisa_verticales()
        juego.revisa_diagonales()
        ###
        juego.jugarRaton()
        ###
        winers = []
        losers = []
        listap = []
        listag = []
        listagstr = []
        listapstr = []
        ###
        tablero = repr(juego)
        print(tablero)
        ###
        final = juego.indicarEstado()
        if final == 1:
            print("Se ha finalizado en un empate")
            n = input()
            break
        if final == 2:
            print("ganaste")
            n = input()
            break
        if final == 3:
            print("perdiste")
            n = input()
            break