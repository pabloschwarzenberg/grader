class Sopa():
    def __init__(self,sopaletras):
        self.tablero=[]
        self.sopaletras=sopaletras

    def cargar_tablero(self,archivo):
        file = open(archivo,"r")

        for line in file:
            lista=line.strip().split(" ")
            self.tablero.append(lista)

        file.close()

    def buscar(self,palabras):
        for palabra in palabras:
            self.derecha(palabra)
            self.abajo(palabra)
            self.diago(palabra)
            self.derecha_inv(palabra)


    def __repr__(self):
        s=""

        for line in self.tablero:
            for letra in line:
                s+="{:<2}".format(letra)
            s+="\n"

        return s

    def derecha(self,palabra):
        k=0
        while k<len(self.tablero):
            i=0
            j=0
            x=0
            ayuda=""

            while j<len(palabra) and i<len(self.tablero[k]):

                if palabra[j]==self.tablero[k][i]:
                    ayuda+=self.tablero[k][i]
                    if j==0:
                        x=i
                    j+=1
                    i+=1
                else:
                    i+=1

            if ayuda==palabra:
                y=k
                posicion=[x+1,y+1]
                print("{},{},{}".format(palabra,posicion,"derecha"))

            k+=1

    def derecha_inv(self,palabra):
        j=0

        while j<len(self.tablero):
            k=0
            i=len(self.tablero)-1

            x=0
            ayuda=""

            while k<len(palabra) and i>0:

                if palabra[k]==self.tablero[j][i]:
                    ayuda+=self.tablero[j][i]

                    if k==0:
                        x=i

                    k+=1
                    i-=1

                else:
                    i-=1

            if ayuda==palabra:
                y=j
                posicion=[x+1,y+1]
                print("{},{},{}".format(palabra,posicion,"derecha_inv"))

            j+=1

    def abajo(self,palabra):

        j=0
        while j<len(self.tablero[0]):
            k=0
            i=0
            ayuda=""

            while k<len(palabra) and i<len(self.tablero):
                if palabra[k]==self.tablero[i][j]:

                    ayuda+=self.tablero[i][j]

                    if k==0:
                        y=i
                    k+=1
                    i+=1

                else:
                    i+=1

            if ayuda==palabra:
                x=j
                posicion=[x+1,y+1]
                print("{},{},{}".format(palabra,posicion,"abajo"))

            j+=1

    def diago(self,palabra):
        j=0
        k=0
        while j<len(self.tablero):
            ayuda=""
            if palabra[k]==self.tablero[j][j]:
                ayuda+=self.tablero[j][j]

                if k==0:
                    y=j
                    x=j

                k+=1
                j+=1
            else:
                j+=1

        if ayuda==palabra:
            posicion=[x+1,y+1]
            print("{},{},{}".format(palabra,posicion,"Diagonal"))



if __name__=="__main__":
    pass

           