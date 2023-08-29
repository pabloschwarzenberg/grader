__version__ = "1.0"
import analizador.util
import tema10_ej1.solucion
import tema10_ej1.plantilla
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        n1=random.randint(10,30)
        n2=random.randint(10,30)
        e=tema10_ej1.solucion.mcm(n1,n2,n1*n2)
        o=self.modulo.mcm(n1,n2,n1*n2)
        if e!=o:
            self.errores.append("El mcm entre {0} y {1} es {2}".format(n1,n2,e))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema10_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)