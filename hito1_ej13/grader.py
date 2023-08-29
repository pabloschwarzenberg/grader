import analizador.util
import io
import sys
import random

def convertir(s):
    for i in range(len(s)):
        c=ord(s[i])
        if c>=48 and c<=57:
            return s[i:]
    return ""

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.primos=[2,3,5,7,11,13]
        n1=random.choice(self.primos)
        n2=random.choice(self.primos)
        n3=random.choice(self.primos)
        self.setup=[[2],[n1*n2*n3],[22]]
        r=[n1,n2,n3]
        r.sort()
        self.output=[[2],r,[2,11]]
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
        salidas=salida.split("\n")
        factores=[]
        for linea in salidas:
            s=convertir(linea)
            try:
                n=int(s)
                factores.append(n)
            except:
                n=0
        if len(factores)!=len(self.output[i]):
            self.errores.append("Al ingresar {0} tu programa debe imprimir {1}".format(
                self.setup[i][0],
                self.output[i]
            ))
        for item in self.output[i]:
            if item in factores:
                p=factores.index(item)
                factores.pop(p)
        if len(factores)!=0:
            self.errores.append("Al ingresar {0} tu programa debe imprimir {1}".format(
                self.setup[i][0],
                self.output[i]
            ))

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