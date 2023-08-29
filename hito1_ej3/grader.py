import analizador.util
import io
import sys

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.setup=[
            ["250000","1970","3","11","S","R"],
            ["250000","1970","4","11","C","R"],
            ["350000","1970","4","11","S","U"],
            ["450000","1970","4","11","S","U"],
            ["450000","1970","1","11","C","R"],
        ]
        self.precondiciones=[self.setup_caso1,self.setup_caso2,self.setup_caso3,self.setup_caso4,self.setup_caso5]
        self.revisiones=[self.caso1,self.caso2,self.caso3,self.caso4,self.caso5]

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def setup_caso1(self):
        self.setup_caso(0)

    def setup_caso2(self):
        self.setup_caso(1)

    def setup_caso3(self):
        self.setup_caso(2)

    def setup_caso4(self):
        self.setup_caso(3)

    def setup_caso5(self):
        self.setup_caso(4)

    def caso1(self):
        salida=sys.stdout.getvalue().strip().upper()
        if(salida.find("APROBADO")==-1):
            self.errores.append("Para la combinación {0}, el resultado debe ser APROBADO".format(self.setup[0]))

    def caso2(self):
        salida=sys.stdout.getvalue().strip()
        if(salida.find("APROBADO")==-1):
            self.errores.append("Para la combinación {0}, el resultado debe ser APROBADO".format(self.setup[1]))

    def caso3(self):
        salida=sys.stdout.getvalue().strip()
        if(salida.find("APROBADO")==-1):
            self.errores.append("Para la combinación {0}, el resultado debe ser APROBADO".format(self.setup[2]))

    def caso4(self):
        salida=sys.stdout.getvalue().strip()
        if(salida.find("APROBADO")==-1):
            self.errores.append("Para la combinación {0}, el resultado debe ser APROBADO".format(self.setup[3]))

    def caso5(self):
        salida=sys.stdout.getvalue().strip()
        if(salida.find("APROBADO")==-1):
            self.errores.append("Para la combinación {0}, el resultado debe ser APROBADO".format(self.setup[4]))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)