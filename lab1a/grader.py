import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[
            ["50000","30000","20000","30000","25000","15000"],
            ["50000","30000","20000","20000","5000","5000"],
            ["50000", "20000", "30000", "5000", "10000", "5000"],
            ["80000", "10000", "10000", "80000", "1000", "1000"],
            ["40000", "20000", "40000", "20000", "1000", "20000"],
            ["40000", "20000", "40000", "20000", "1000", "1000"],
        ]
        self.output=[
            ["electa"],
            ["perdedora"],
            ["perdedora"],
            ["electa"],
            ["electa"],
            ["perdedora"]
        ]
        self.precondiciones=[
            self.setup_caso1,self.setup_caso2,self.setup_caso3,
            self.setup_caso4, self.setup_caso5, self.setup_caso6
        ]
        self.revisiones=[
            self.caso1,self.caso2,self.caso3,
            self.caso4, self.caso5, self.caso6
        ]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower().replace(" ","")
        salida.replace("á","a")
        for patron in self.output[i]:
            if salida.find(patron)==-1:
                self.errores.append("Para {0} el resultado esperado es {1}".format(self.setup[i],
                                                                 self.output[i]))
                return

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

    def setup_caso4(self):
        self.setup_caso(3)

    def caso4(self):
        self.revisar_caso(3)

    def setup_caso5(self):
        self.setup_caso(4)

    def caso5(self):
        self.revisar_caso(4)

    def setup_caso6(self):
        self.setup_caso(5)

    def caso6(self):
        self.revisar_caso(5)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)