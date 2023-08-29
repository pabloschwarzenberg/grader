import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.n=random.randint(2,12)

    def iniciar_redireccion(self):
        sys.stdin=io.StringIO("{0}\n".format(self.n))
        sys.stdout=io.StringIO()

    def analizar(self):
        combinaciones=sys.stdout.getvalue()
        combinaciones=combinaciones.strip().split("\n")
        if len(combinaciones)!=2**self.n:
            self.errores.append("La cantidad de combinaciones para n={0} debiera ser {1} no {2}".format(self.n,2**self.n,len(combinaciones)))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)