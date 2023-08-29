import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.n=random.randint(10,100)

    def iniciar_redireccion(self):
        sys.stdin=io.StringIO("{0}\n".format(self.n))
        sys.stdout=io.StringIO()

    def analizar(self):
        salida=sys.stdout.getvalue().strip()
        suma_esperada=int(self.n*(self.n+1)/2);
        if salida.find(str(suma_esperada))==-1:
            self.errores.append("La suma de los n={0} primeros números debiera ser {1} no {2}".format(self.n,
            suma_esperada,salida))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)