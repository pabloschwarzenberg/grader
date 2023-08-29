import analizador.util
import io
import sys

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[["77389909","13"],["98927674","20"],["87765545","18"]]
        self.precondiciones=[self.setup_caso1,self.setup_caso2,self.setup_caso3]
        self.revisiones=[self.caso1,self.caso2,self.caso3]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        sys.stdin.write("{0}\n{1}\n".format(self.setup[i][0],self.setup[i][1]))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def setup_caso1(self):
        self.setup_caso(0)

    def setup_caso2(self):
        self.setup_caso(1)

    def setup_caso3(self):
        self.setup_caso(2)

    def caso1(self):
        salida=sys.stdout.getvalue().strip().upper()
        if(salida.find("NO CONTESTAR")!=-1 or salida.find("CONTESTAR")==-1):
            self.errores.append("Para la combinación {0} la respuesta esperada debiera ser CONTESTAR".format(self.setup[0]))

    def caso2(self):
        salida=sys.stdout.getvalue().strip().upper()
        if(salida.find("NO CONTESTAR")==-1):
            self.errores.append("Para la combinación {0} la respuesta esperada debiera ser NO CONTESTAR".format(self.setup[1]))

    def caso3(self):
        salida=sys.stdout.getvalue().strip().upper()
        if(salida.find("NO CONTESTAR")==-1):
            self.errores.append("Para la combinación {0} la respuesta esperada debiera ser NO CONTESTAR".format(self.setup[2]))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)