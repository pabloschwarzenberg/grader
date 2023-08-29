import analizador.util
import io
import sys

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=\
            [["ACCTGGTTCTGTAGTCAGGATTACTA",
              "TGACGTTCAGTAGTCGATT"]]
        self.output=\
            [["___TG_______A__C_G__TT_C_AGTAGTCGATT"]]
        self.precondiciones=[self.setup_caso1]
        self.revisiones=[self.caso1]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().upper()
        for patron in self.output[i]:
            if salida.find(patron)==-1:
                self.errores.append("Para {0} el resultado esperado es {1}".format(self.setup[i],
                                                                 self.output[i]))
                return

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)