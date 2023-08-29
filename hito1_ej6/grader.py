import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        n1=random.randint(10,100)
        n2=random.randint(10,100)
        n3=random.randint(10,100)
        l1=[n1,n2,n1]
        l2=[n1,n2,n3]
        self.setup=[
            l1.copy(),
            l2.copy()
        ]
        l1.sort()
        l2.sort()
        self.output=[
            ",".join(list(map(str,l1))),
            ",".join(list(map(str,l2)))
                    ]
        self.precondiciones=[self.setup_caso1,self.setup_caso2]
        self.revisiones=[self.caso1,self.caso2]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower().replace(" ","")
        if(salida.find(self.output[i])==-1):
            self.errores.append("Al ingresar {0} tu programa debe imprimir: {1}".format(
                " ".join(list(map(str,self.setup[i]))),
                self.output[i]))

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

    def setup_caso2(self):
        self.setup_caso(1)

    def caso2(self):
        self.revisar_caso(1)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)