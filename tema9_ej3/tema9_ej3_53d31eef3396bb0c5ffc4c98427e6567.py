def decodificar(mensaje):
    return mensaje
def decodificar(mensaje):

    a = str(mensaje[0:8])

    decimal1=(int(str(a), 2))

    letra1=chr(decimal1)

    b = str(mensaje[10:17])

    decimal2=(int(str(b), 2))

    letra2=chr(decimal2)

    c = str(mensaje[19:26])

    decimal3=(int(str(c), 2))

    letra3=chr(decimal3)

    d = str(mensaje[28:35])

    decimal4=(int(str(d), 2))

    letra4=chr(decimal4)

    palabra = letra1+letra2+letra3+letra4

    return palabra
#########
class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0],
             self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]],
             [self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0],
             self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]]])
          return m