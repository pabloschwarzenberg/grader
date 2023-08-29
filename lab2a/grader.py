import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        x=2
        y=7
        self.setup=[]
        self.output=[]
        for i in range(4):
            inicio=random.randint(1,6)
            fin=random.randint(50,100)
            self.setup.append([str(inicio),str(fin)])
            self.output.append([self.divisores_conjuntos(inicio,fin,x,y)])
        self.setup.append([str(-100),str(-50)])
        self.output.append([self.divisores_conjuntos(-100,-50,x,y)])
        self.setup.append([str(10),str(0)])
        self.output.append([""])
        self.precondiciones=[
            self.setup_caso1,self.setup_caso2,self.setup_caso3,
            self.setup_caso4, self.setup_caso5, self.setup_caso6
        ]
        self.revisiones=[
            self.caso1,self.caso2,self.caso3,
            self.caso4, self.caso5, self.caso6
        ]

    def divisores_conjuntos(self,inicio,fin,x,y):
        i=inicio
        s=""
        while i<=fin:
            if i%x==0 and i%y==0:
                if s=="":
                    s=str(i)
                else:
                    s=s+"\n"+str(i)
            i=i+1
        return s

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