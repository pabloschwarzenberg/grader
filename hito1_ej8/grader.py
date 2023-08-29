import analizador.util
import io
import sys
import random

def descomponer(numero):
    s=str(numero)
    r=""
    signo=["U","D","C","M"]
    n=len(s)
    for i in range(n):
        if i==0:
            r=s[i]+signo[n-i-1]
        else:
            r=r+"+"+s[i]+signo[n-i-1]
    return r.strip()

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        n1=random.randint(1,999)
        n2=random.randint(1000,10000)
        self.setup=[
            [n1],
            [n2]
        ]
        self.output=[
            descomponer(n1),
            descomponer(n2)
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
        salida=sys.stdout.getvalue().strip().upper().replace(" ","")
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