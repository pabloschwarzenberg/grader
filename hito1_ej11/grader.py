import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        b1=random.choice([20000,10000,5000])
        b2=random.choice([10000,5000])
        c1=random.randint(1,4)
        c2=random.randint(1,5)
        monto=b1*c1+b2*c2
        if monto>100000:
            monto=100000
        self.setup=[["10334151","1803",str(monto),"Y"]]
        self.output=[["saldo cuenta={0}".format(100000-monto),
                      "saldo cajero={0}".format(1000000-monto)]]
        self.precondiciones=[self.setup_caso1]
        self.revisiones=[self.caso1]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower().replace(" ","")
        for item in self.output[i]:
            item=item.replace(" ","")
            if(salida.find(item)==-1):
                self.errores.append("Al ingresar {0} tu programa debe imprimir: {1}".format(
                    " ".join(list(map(str,self.setup[i]))),
                    self.output[i]))
                break
        salidas=salida.split("\n")
        billetes=[]
        monto=0
        for linea in salidas:
            p=linea.find("billetes")
            if p!=-1:
                billetes.append(linea)
                valores=linea.split("=")
                try:
                    monto=monto+int(valores[0][p+8:])*int(valores[1])
                except:
                    monto = 0
                    break
        if monto!=int(self.setup[i][2]):
            if len(billetes)==0:
               self.errores.append("Tu programa no imprime el detalle de billetes")
            else:
                self.errores.append("La suma de billetes debiera ser {0} pero tu programa muestra: {1}".format(
                self.setup[i][2],billetes))

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)