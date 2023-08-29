import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[["actgacac"],["actgb"],["ACTG"]]
        self.output=["correcta","incorrecta","correcta"]
        self.precondiciones=[self.setup_caso1,self.setup_caso2,self.setup_caso3]
        self.revisiones=[self.caso1,self.caso2,self.caso3]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower().replace(" ","")
        salida.replace("á","a")
        if salida.find(self.output[i])==-1:
            self.errores.append("La secuencia {0} es {1}".format(self.setup[i][0],
                                                                 self.output[i]))

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

    def setup_caso2(self):
        self.setup_caso(1)

    def caso2(self):
        self.revisar_caso(1)

    def setup_caso3(self):
        self.setup_caso(2)

    def caso3(self):
        self.revisar_caso(2)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)