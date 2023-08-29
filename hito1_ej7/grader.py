import analizador.util
import io
import sys
import random

signos=[
    ["aries",21,3,20,4],
    ["tauro",21,4,21,5],
    ["geminis",22,5,21,6],
    ["cancer",22,6,22,7],
    ["leo",23,7,22,8],
    ["virgo",23,8,23,9],
    ["libra",24,9,23,10],
    ["escorpio",24,10,22,11],
    ["sagitario",23,11,21,12],
    ["capricornio",22,12,20,1],
    ["acuario",21,1,19,2],
    ["piscis",20,2,20,3]
]

def encontrar_signo(dia,mes):
    for signo in signos:
        if mes==signo[2] or mes==signo[4]:
            if mes==signo[2] and dia>=signo[1]:
                return signo[0]
            if mes==signo[4] and dia<=signo[3]:
                return signo[0]
    return "error"

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        m1=random.randint(1,12)
        d1=random.randint(1,28)
        m2=random.randint(1,12)
        d2=random.randint(1,28)
        self.setup=[
            [d1,m1],
            [d2,m2]
        ]
        self.output=[
            encontrar_signo(d1,m1),
            encontrar_signo(d2,m2)
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