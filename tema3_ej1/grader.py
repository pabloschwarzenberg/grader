__version__ = "1.0"
import analizador.util
import tema3_ej1.solucion
import tema3_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        r1=self.modulo.suma_divisores(1)
        r2=tema3_ej1.solucion.suma_divisores(1)
        if r1!=r2:
            self.errores.append("Para el número 1, tu función debiera retornar {0}".format(r2))

        r1=self.modulo.suma_divisores(8)
        r2=tema3_ej1.solucion.suma_divisores(8)
        if r1!=r2:
            self.errores.append("Para el número 8, tu función debiera retornar {0}".format(r2))

        r1=self.modulo.suma_divisores(13)
        r2=tema3_ej1.solucion.suma_divisores(13)
        if r1!=r2:
            self.errores.append("Para el número 13, tu función debiera retornar {0}".format(r2))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema3_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)