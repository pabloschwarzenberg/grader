import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[]
        self.output=[]
        n=random.randint(3,10)
        numeros=[]
        for i in range(n):
            valor=random.randint(1,7)
            numeros.append(valor)
        cantidad=len(numeros)
        suma=sum(numeros)
        promedio=round(suma/cantidad,1)
        minimo=min(numeros)
        maximo=max(numeros)
        numeros=list(map(str,numeros))
        numeros.append(str(-1))
        self.setup.append(numeros)
        self.output.append(["cantidad={}".format(cantidad),"suma={}".format(suma),"maximo={}".format(maximo)])
        self.setup.append([str(2),str(2),str(-1)])
        self.output.append(["cantidad={}".format(2),"suma={}".format(4),"maximo={}".format(2)])
        self.setup.append([str(-1)])
        self.output.append(["cantidad={}".format(0),"suma=0","maximo=nd"])
        self.precondiciones=[
            self.setup_caso1,self.setup_caso2,self.setup_caso3
        ]
        self.revisiones=[
            self.caso1,self.caso2,self.caso3
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

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)