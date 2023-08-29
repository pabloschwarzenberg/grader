import analizador.util
import io
import sys

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[["10334151","1803","45000","Y"]]
        self.output=[["saldo cuenta=55000","saldo cajero=955000"]]
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

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)