__version__ = "1.0"
import analizador.util
import random
import tema2_ej3.solucion
import tema2_ej3.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        n=random.choice([3,5,7])
        perfecto=2**(n-1)*(2**n-1)
        r1=self.modulo.numero_perfecto(6)
        if r1!=True:
            self.errores.append("El número 6 es perfecto, pero tu función retorna {0}".format(r1))

        r1=self.modulo.numero_perfecto(8)
        if r1!=False:
            self.errores.append("El número 8 no es perfecto, pero tu función retorna {0}".format(r1))

        r1=self.modulo.numero_perfecto(perfecto)
        if r1!=True:
            self.errores.append("El número {0} es perfecto, pero tu función retorna {1}".format(perfecto,r1))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema2_ej3.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)